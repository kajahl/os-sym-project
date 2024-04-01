import abc
from src.processor.objects.Process import Process
from src.processor.objects.ProcessorTestResult import ProcessorTestResult
from src.processor.objects.ProcessorTestCase import ProcessorTestCase

class BaseProcessor(abc.ABC):
    def __init__(self):
        # Aktualne dane testu
        self._currentTestId: str = ""
        # Lista procesów - Indeks powinien odpowiadać ID procesu
        self._processes: list[Process] = []
        # Aktualny czas
        self._currentTime: int = 0
        # Oś czasu wykonywania procesów
        self._executingTimeline: list[int] = []
        return 

    # Sprawdzenie błędów - ID procesu powinno odpowiadać indeksowi w liście
    def _checkErrors(self) -> None:
        for i in range(0, len(self._processes)):
            if self._processes[i].getProcessId() != i:
                raise Exception("Invalid process ID")

    # Załadowanie testu
    def loadTestCase(self, testCase: ProcessorTestCase) -> None:
        self.resetProcessor()
        self._currentTestId = testCase.getID()
        self.setProcesses(testCase.getProcesses())

    # Ustawienie procesów
    def setProcesses(self, processes: list[Process]) -> None:
        self._processes = processes
        self._checkErrors()

    # Zwrócenie listy procesów
    def getProcesses(self) -> list[Process]:
        return self._processes
    
    # Zwrócenie listy procesów, które są dostępne do wykonania
    def getAvalibleProcesses(self) -> list[Process]:
        return [process for process in self.getProcesses() if process.isProcessCame(self._currentTime) and not process.isProcessDone()]

    # Resetowanie procesora
    def resetProcessor(self) -> None:
        self._currentTestId = ""
        self._currentTime = 0
        self._processes = []
        self._executingTimeline = []

    # Zwrócenie ID procesu, który powinien zostać wykonany
    @abc.abstractmethod
    def _getNextProcessId(self) -> int:
        pass

    # Zwrócenie nazwy procesora
    # Rename to getShortcut?
    @abc.abstractmethod
    def getName(self) -> str:
        pass

    # Sprawdzenie czy symulacja się zakończyła
    def _isSimulationDone(self) -> bool:
        return len([process for process in self._processes if not process.isProcessDone()]) == 0

    # Zwrócenie procesu na podstawie ID
    def _getProcess(self, processId) -> Process:
        return self._processes[processId]

    # Wykonanie następnego procesu
    def _executeNextProcess(self) -> None:
        # Pobranie ID procesu, który powinien zostać wykonany
        nextProcessId = self._getNextProcessId()
        # Pobranie procesu
        process = self._getProcess(nextProcessId)
        # Wykonywanie procesu do momentu, aż się nie skończy
        while not process.isProcessDone():
            # Wykonanie procesu w danym czasie
            process.executeProcess(self._currentTime)
            # Dodanie procesu do osi czasu
            self._executingTimeline.append(nextProcessId)
            # Zwiększenie czasu
            self._currentTime += 1

    # Uruchomienie symulacji
    def runSimulation(self) -> None:
        # Wykonanie procesów do momentu, aż się nie skończą
        while not self._isSimulationDone():
            self._executeNextProcess()

    # Zwrócenie wyniku
    def getResult(self) -> ProcessorTestResult:
        rawdata = ' '.join(list(map(str, self._executingTimeline))) + "\n" + ' '.join(list(map(str, [process.getTotalWaitingTime() for process in self._processes]))) + "\n" + str(sum([process.getTotalWaitingTime() for process in self._processes])/len(self._processes))
        return ProcessorTestResult(self._currentTestId, self.getName(), rawdata)