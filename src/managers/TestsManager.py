from src.managers.FileManager import FileManager
from src.processor.objects.ProcessorTestCase import ProcessorTestCase
from src.ram.objects.MemoryTestCase import MemoryTestCase
from src.processor.objects.ProcessorTestResult import ProcessorTestResult
from src.ram.objects.MemoryTestResult import MemoryTestResult
from src.objects.SummaryTable import SummaryTable

class TestsManager:
    """
    This class is responsible for managing the tests.
    
    [PL]
    Klasa odpowiedzialna za zarządzanie testami.
    Klasa sama w sobie nie jest odpowiedzialna w żadne sposób za tworzenie plików/przypadków testowych
    Klasa wczytuje dane z plików i zwraca je w odpowiedniej formie. (zwraca TestCase z pomocą gettera)
    Klasa przechowuje dane po wykonaniu algorytmu i przechowuje je w odpowiedniej formie (TestCaseResult) oraz zapisuje je na dysku.
    """

    def __init__(self):
        # Przypadki testowe dla procesora
        self._processorTests : list[ProcessorTestCase] = self._loadTests(FileManager.getProcessorTests(), FileManager.getProcessorFolderName(), ProcessorTestCase)
        self._processorTestsResults : list[ProcessorTestResult] = self._loadResults(FileManager.getProcessorTestsResults(), FileManager.getProcessorFolderName(), ProcessorTestResult)

        # Przypadki testowe dla pamięci
        self._memoryTests : list[MemoryTestCase] = self._loadTests(FileManager.getMemoryTests(), FileManager.getMemoryFolderName(), MemoryTestCase)
        self._memoryTestsResults : list[MemoryTestResult] = self._loadResults(FileManager.getMemoryTestsResults(), FileManager.getMemoryFolderName(), MemoryTestResult)

    # Może być static, ale instancja TestsManager jest tylko jedna
    def _loadTests(self, filenames: list[str], folderName: str, testCaseClass: type):
        tests = []
        for filename in filenames:
            rawData = FileManager.readFile(FileManager.joinPath(FileManager.getInputPath(), folderName), filename)
            testCase = testCaseClass(filename, FileManager.removeComments(rawData))
            tests.append(testCase)
        return tests
    
    # Może być static, ale instancja TestsManager jest tylko jedna
    def _loadResults(self, filenames: list[str], folderName: str, testResultClass: type):
        results = []
        # Filter only .txt files with pattern {algoShortcut}_{testId}.txt
        filenames = [x for x in filenames if x.endswith(".txt") and "_" in x]
        for filename in filenames:
            # name convention: {algoShortcut}_{testId}.txt
            algoShortcut, testId = filename.split("_")
            testId = testId.split(".")[0]
            rawData = FileManager.readFile(FileManager.joinPath(FileManager.getOutputPath(), folderName), filename)
            testResult = testResultClass(testId, algoShortcut, FileManager.removeComments(rawData))
            results.append(testResult)
        return results

    def saveResults(self):
        for result in self._processorTestsResults:
            filename = f"{result.algoShortcut}_{result.testId}.txt"
            FileManager.writeFile(FileManager.joinPath(FileManager.getOutputPath(), FileManager.getProcessorFolderName()), filename, str(result))
        for result in self._memoryTestsResults:
            filename = f"{result.algoShortcut}_{result.testId}.txt"
            FileManager.writeFile(FileManager.joinPath(FileManager.getOutputPath(), FileManager.getMemoryFolderName()), filename, str(result))

    # Processor tests
    def getProcessorTests(self) -> list[ProcessorTestCase]:
        return self._processorTests
    
    def getProcessorTest(self, index: int) -> ProcessorTestCase:
        return self._processorTests[index]
    
    def getProcessorTestById(self, id: str) -> ProcessorTestCase:
        for test in self._processorTests:
            if test.getID() == id:
                return test
        return None
    
    def setProcessorTestResult(self, result: ProcessorTestResult):
        self._processorTestsResults.append(result)

    def getProcessorTestResults(self) -> list[ProcessorTestResult]:
        return self._processorTestsResults
    
    def getProcessorTestResultsById(self, testId: str) -> list[ProcessorTestResult]:
        return [x for x in self._processorTestsResults if x.testId == testId]
    
    def getProcessorTestResult(self, testId: str, algoShortcut: str) -> ProcessorTestResult:
        for result in self._processorTestsResults:
            if result.testId == testId and result.algoShortcut == algoShortcut:
                return result
        return None
    
    # Memory tests
    def getMemoryTests(self) -> list[MemoryTestCase]:
        return self._memoryTests
    
    def getMemoryTest(self, index: int) -> MemoryTestCase:
        return self._memoryTests[index]
    
    def getMemoryTestById(self, id: str) -> MemoryTestCase:
        for test in self._memoryTests:
            if test.getID() == id:
                return test
        return None
    
    def setMemoryTestResult(self, result: MemoryTestResult):
        self._memoryTestsResults.append(result)

    def getMemoryTestResults(self) -> list[MemoryTestResult]:
        return self._memoryTestsResults
    
    def getMemoryTestResult(self, testId: str, algoShortcut: str) -> MemoryTestResult:
        for result in self._memoryTestsResults:
            if result.testId == testId and result.algoShortcut == algoShortcut:
                return result
        return None
    
    def getMemoryTestResultsById(self, testId: str) -> list[MemoryTestResult]:
        return [x for x in self._memoryTestsResults if x.testId == testId]
    
    # Wygenerowanie podsumowania dla procesorów
    def generateProcessorSummary(self):
        # if Main.isVerbose(): print(f"Generowanie podsumowania dla procesorów")

        # Dodatkowe kolumny
        MIN_EXE_TIME = "MinExeTime"
        AVG_EXE_TIME = "AvgExeTime"
        MAX_EXE_TIME = "MaxExeTime"
        MIN_ARR_TIME = "MinArrTime"
        AVG_ARR_TIME = "AvgArrTime"
        MAX_ARR_TIME = "MaxArrTime"

        # Ustawianie tabeli
        table = SummaryTable()
        processorTestIds = list(set([x.getID() for x in self.getProcessorTests()]))
        table.setRows(processorTestIds)
        processorAlgoNames = list(set([x.algoShortcut for x in self.getProcessorTestResults()]))
        table.setColumns([MIN_EXE_TIME, AVG_EXE_TIME, MAX_EXE_TIME, MIN_ARR_TIME, AVG_ARR_TIME, MAX_ARR_TIME] + processorAlgoNames)

        # Wypełnianie tabeli
        table.fillValues("0")
        for processorTestId in processorTestIds:
            # Dane pojedynczego testu
            testCase = self.getProcessorTestById(processorTestId)
            arrTimes = testCase.getProcessArrivalRange()
            exeTimes = testCase.getProcessDurationRange()
            table.setValue(MIN_EXE_TIME, processorTestId, f"{exeTimes[0]}")
            table.setValue(MAX_EXE_TIME, processorTestId, f"{exeTimes[1]}")
            table.setValue(AVG_EXE_TIME, processorTestId, f"{testCase.getAvgExecutionTime():.2f}")
            table.setValue(AVG_ARR_TIME, processorTestId, f"{testCase.getAvgArrivalTime():.2f}")
            table.setValue(MIN_ARR_TIME, processorTestId, f"{arrTimes[0]}")
            table.setValue(MAX_ARR_TIME, processorTestId, f"{arrTimes[1]}")
            # Wiersze - dla każdego algorytmu
            for processorAlgo in processorAlgoNames:
                result = self.getProcessorTestResult(processorTestId, processorAlgo)
                table.setValue(processorAlgo, processorTestId, f"{result.getAvgWaitingTime():.2f}")
                # Print do sprawozdania - do tabelki
                # print(f"{processorAlgo} {processorTestName} - Ilość procesów: {test.getProcessesCount()}\nŚredni czas oczekiwania: {result.getAvgWaitingTime():.2f}\nŚredni czas wykonywania: {test.getAvgExecutionTime():.2f}\n\nCzasy przyjścia: [{arrTimes[0]}, {arrTimes[1]}]\nCzasy wykonania: [{exeTimes[0]}, {exeTimes[1]}]")
        
        # Zapis tabeli
        fullPath = FileManager.joinPath(FileManager.getOutputPath(), FileManager.getProcessorFolderName())
        fileName = "processor-summary.txt"
        FileManager.writeFile(fullPath, fileName, str(table.getTable()))
        # if Main.isVerbose(): print(f"Podsumowanie dla procesorów zapisano w pliku {fileName} w folderze {fullPath}")
    
    # Wygenerowanie podsumowania dla procesorów
    def generateRamSummary(self):
        # if Main.isVerbose(): print(f"Generowanie podsumowania dla pamięci")

        # Dodatkowe kolumny
        MEMORY_SIZE = "MemSize"
        UNIQUE_PROCESS_COUNT = "UniqProcCount"
        QUEUE_LEN = "QueLen"

        # Wypełnianie tabeli
        table = SummaryTable()
        memoryTestIds = list(set([x.getID() for x in self.getMemoryTests()]))
        table.setRows(memoryTestIds)
        ramAlgoNames = list(set([x.algoShortcut for x in self.getMemoryTestResults()]))
        table.setColumns([MEMORY_SIZE, UNIQUE_PROCESS_COUNT, QUEUE_LEN] + ramAlgoNames)
        table.fillValues("0")

        # Wypełnianie tabeli
        for memoryTestId in memoryTestIds:
            testCase = self.getMemoryTestById(memoryTestId)
            table.setValue(MEMORY_SIZE, memoryTestId, f"{testCase.getMemorySize()}")
            table.setValue(UNIQUE_PROCESS_COUNT, memoryTestId, f"{testCase.getUniuqePagesCount()}")
            table.setValue(QUEUE_LEN, memoryTestId, f"{len(testCase.getPageAccessQueue())}")
            # Wiersze - dla każdego algorytmu
            for ramAlgo in ramAlgoNames:
                result = self.getMemoryTestResult(memoryTestId, ramAlgo)
                table.setValue(ramAlgo, memoryTestId, f"{result.getErrorCounter()}")

        # Zapis tabeli
        fullPath = FileManager.joinPath(FileManager.getOutputPath(), FileManager.getMemoryFolderName())
        fileName = "memory-summary.txt"
        FileManager.writeFile(fullPath, fileName, table.getTable().to_string())
        
