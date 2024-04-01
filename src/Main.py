from src.managers.FileManager import FileManager
from src.managers.PlotManager import PlotManager
from src.managers.TestsManager import TestsManager
# Procesory
from src.processor.BaseProcessor import BaseProcessor
from src.processor.FCFSProcessor import FCFSProcessor
from src.processor.LCFSProcessor import LCFSProcessor
from src.processor.SJFProcessor import SJFProcessor
from src.processor.objects.ProcessorTestCase import ProcessorTestCase
# Pamięć
from src.ram.BaseMemory import BaseMemory
from src.ram.FIFOMemory import FIFOMemory
from src.ram.LRUMemory import LRUMemory
from src.ram.LFUMemory import LFUMemory
from src.ram.objects.MemoryTestCase import MemoryTestCase
# Generowanie readme
from src.generators.ReadmeGenerator import ReadmeGenerator

# Enum dla typu algorytmu
from enum import Enum
class AlgorithmType(Enum):
    PROCESSOR = 1
    MEMORY = 2

# Główna klasa
class Main:
    _VERBOSE = False
    @staticmethod
    def isVerbose() -> bool:
        return Main._VERBOSE

    def __init__(self, verbose: bool = False):
        FileManager.createRequiredFolders()
        self.processorAlgorithms: list[BaseProcessor] = [FCFSProcessor(), LCFSProcessor(), SJFProcessor()]
        self.memoryAlgorithms: list[BaseMemory] = [FIFOMemory(), LRUMemory(), LFUMemory()]
        self.testManager = TestsManager()
        Main._VERBOSE = verbose

    def save(self):
        self.testManager.saveResults()

    # Uruchomienie symulacji
    def runAllSimulations(self):
        if Main.isVerbose(): print(f"Uruchamianie symulacji dla procesorów i pamięci")
        self.runProcessorSimulations()
        self.runRamSimulations()

    def runProcessorSimulations(self):
        if Main.isVerbose(): print(f"Uruchamianie symulacji dla procesorów")
        for processorTest in self.testManager.getProcessorTests():
            self._runProcessorTest(processorTest)
        self.testManager.saveResults()

    def runRamSimulations(self):
        if Main.isVerbose(): print(f"Uruchamianie symulacji dla pamięci")
        for memoryTest in self.testManager.getMemoryTests():
            self._runMemoryTest(memoryTest)
        self.testManager.saveResults()

    # Generowanie wykresów
    def makeAllGraphs(self):
        if Main.isVerbose(): print(f"Generowanie wykresów dla procesorów i pamięci")
        self.makeProcessorGraphs()
        self.makeRamGraphs()

    def makeProcessorGraphs(self):
        if Main.isVerbose(): print(f"Generowanie wykresów dla procesorów")
        for processorResult in self.testManager.getProcessorTestResults():
            PlotManager.makeProcessorGraph(self.testManager.getProcessorTestById(processorResult.testId), processorResult)

    def makeRamGraphs(self):
        if Main.isVerbose(): print(f"Generowanie wykresów dla pamięci")
        for memoryResult in self.testManager.getMemoryTestResults():
            PlotManager.makeMemoryGraph(self.testManager.getMemoryTestById(memoryResult.testId), memoryResult)

    # Generowanie podsumowania
    def generateAllSummary(self):
        if Main.isVerbose(): print(f"Generowanie podsumowania dla procesorów i pamięci")
        self.testManager.generateProcessorSummary()
        self.testManager.generateRamSummary()

    def generateAllReadme(self):
        if Main.isVerbose(): print(f"Generowanie plików readme dla procesorów i pamięci")
        self.generateProcessorReadme()
        self.generateMemoryReadme()

    def generateProcessorReadme(self):
        if Main.isVerbose(): print(f"Generowanie plików readme dla procesorów")
        for test in self.testManager.getProcessorTests():
            ReadmeGenerator.generateProcessorReadme(
                FileManager.joinPath(FileManager.getOutputPath(), FileManager.getProcessorFolderName()),
                test.getID(), 
                self.testManager
            )
        ReadmeGenerator.generateSummaryReadme(FileManager.joinPath(FileManager.getOutputPath(), FileManager.getProcessorFolderName()))

    def generateMemoryReadme(self):
        if Main.isVerbose(): print(f"Generowanie plików readme dla pamięci")
        for test in self.testManager.getMemoryTests():
            ReadmeGenerator.generateMemoryReadme(
                FileManager.joinPath(FileManager.getOutputPath(), FileManager.getMemoryFolderName()),
                test.getID(), 
                self.testManager
            )
        ReadmeGenerator.generateSummaryReadme(FileManager.joinPath(FileManager.getOutputPath(), FileManager.getMemoryFolderName()))

    # Uruchomienie testu dla procesora
    def _runProcessorTest(self, testCase: ProcessorTestCase):
        if Main.isVerbose(): print(f"Uruchamianie testu {testCase.fileName} dla algorytmów procesora")
        # Uruchomienie testu dla każdego algorytmu
        for processorAlgorithm in self.processorAlgorithms:
            # Log
            if Main.isVerbose(): print(f"Uruchamianie testu {testCase.fileName} dla algorytmu {processorAlgorithm.getName()}")
            # Załadowanie przypadku testowego
            processorAlgorithm.loadTestCase(testCase)
            # Uruchomienie symulacji
            processorAlgorithm.runSimulation()
            # Pobranie wyników
            result = processorAlgorithm.getResult()
            # Zapis wyników do test managera
            self.testManager.setProcessorTestResult(result)
            # Log
            if Main.isVerbose(): print(f"Zakończono test {testCase.fileName} dla algorytmu {processorAlgorithm.getName()}")
        return

    # Uruchomienie testu dla pamięci
    def _runMemoryTest(self, testCase: MemoryTestCase):
        if Main.isVerbose(): print(f"Uruchamianie testu {testCase.fileName} dla algorytmów pamięci")
        for memoryAlgorithm in self.memoryAlgorithms:
            # Log
            if Main.isVerbose(): print(f"Uruchamianie testu {testCase.fileName} dla algorytmu {memoryAlgorithm.getName()}")
            # Załadowanie przypadku testowego
            memoryAlgorithm.loadTestCase(testCase)
            # Uruchomienie symulacji
            memoryAlgorithm.runSimulation()
            # Pobranie wyników
            result = memoryAlgorithm.getResult()
            # Zapis wyników do test managera
            self.testManager.setMemoryTestResult(result)
            # Log
            if Main.isVerbose(): print(f"Zakończono test {testCase.fileName} dla algorytmu {memoryAlgorithm.getName()}")
        return