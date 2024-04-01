from src.processor.objects.Process import Process
from src.objects.ATestCase import ATestCase
from src.managers.FileManager import FileManager

class ProcessorTestCase(ATestCase):
    def __init__(self, fileName: str, rawData: str):
        super().__init__(fileName)
        lines = rawData.split("\n")
        # ID
        self._id = lines[0]
        # Sprawdzanie poprawnosci id - id bedzie nazwa pliku, wiec nie moze zawierac wielu znakow
        if not self._id.isalnum():
            raise Exception(f"Invalid ID in test {fileName}")
        # Nazwa testu
        self.testName = lines[1]
        # Opis testu
        self.testDescription = lines[2]
        # Dane procesów
        self.processesRawData = lines[3:]

    # Zwróć ID
    def getID(self) -> str:
        return self._id

    # Zwróć ilość procesów
    def getProcessesCount(self) -> int:
        return len(self.processesRawData)
    
    # Zwróć przedział czasu przyjścia procesów
    def getProcessArrivalRange(self) -> tuple[int, int]:
        return min([x.getProcessArrival() for x in self.getProcesses()]), max([x.getProcessArrival() for x in self.getProcesses()])
    
    # Zwróć przedział czasu trwania procesów
    def getProcessDurationRange(self) -> tuple[int, int]:
        return min([x.getProcessDuration() for x in self.getProcesses()]), max([x.getProcessDuration() for x in self.getProcesses()])

    # Zwróć listę procesów do testów
    def getProcesses(self) -> list[Process]:
        processes = []
        id = 0
        # Tworzenie procesów na podstawie danych
        for processRawData in self.processesRawData:
            processRawData = processRawData.split(" ")
            processArrival = int(processRawData[0])
            processDuration = int(processRawData[1])
            processes.append(Process(id, processArrival, processDuration))
            id += 1
        return processes
    
    # Formatowanie wyniku
    def formatResult(self, result: str) -> str:
        return f"{result}"
    
    # Zwrócenie średni czasu przyjścia
    def getAvgArrivalTime(self) -> float:
        return sum([x.getProcessArrival() for x in self.getProcesses()]) / self.getProcessesCount()
    
    # Zwrócenie średni czasu trwania
    def getAvgExecutionTime(self) -> float:
        return sum([x.getProcessDuration() for x in self.getProcesses()]) / self.getProcessesCount()
    
    # Opis
    def __str__(self) -> str:
        return f"ProcessorTest - {self.testName}\nDescription: {self.testDescription}\nProcesses: {self.processesRawData}"
    
    # Zapisanie testu do pliku
    @staticmethod
    def create(fileName: str, title: str, description: str, processes: list[Process]):
        # Stworzenie zapisu tekstowego
        content = ""
        content += f"{title}\n"
        content += f"{description}\n"
        for process in processes:
            content += f"{process.getProcessArrival()} {process.getProcessDuration()}\n"
        # Zapianie do pliku
        fullPath = FileManager.joinPath(FileManager.getInputPath(), FileManager.getProcessorFolderName())
        FileManager.writeFile(fullPath, fileName, content)
        print(f"Utworzono test {fileName} w {fullPath}")