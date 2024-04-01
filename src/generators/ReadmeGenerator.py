from src.managers.FileManager import FileManager
from src.managers.TestsManager import TestsManager

class ReadmeGenerator:
    @staticmethod
    def generateSummaryReadme(path: str):
        readmeFiles = FileManager.getFiles(path, ".md")

        readme = "# Comparisons in specific tests\n\n"

        for readmeFile in readmeFiles:
            readme += f"[{readmeFile}](./{readmeFile})\n\n"

        FileManager.writeFile(path, "readme.md", readme)

    @staticmethod
    def generateProcessorReadme(path: str, testCaseId: int, testsManager: TestsManager):
        
        # Struktura
        # - Nazwa testu
        # - Opis testu
        # - Dane wejściowe
        # - Dla każdego algorytmu:
        #   - Dane wyjściowe
        #   - Wykresy
        #   - Opis
        # - Podsumowanie dla wszystkich algorytmów

        # Back to previous readme href
        readme = "[Back to summary](./readme.md)\n\n"

        testCase = testsManager.getProcessorTestById(testCaseId)
        testResults = testsManager.getProcessorTestResultsById(testCaseId)

        # Nazwa testu
        readme += f"# Test {testCase.testName}\n"

        # Opis testu
        readme += f"## Test description\n"
        readme += f"{testCase.testDescription}\n"
        
        # Dane wejściowe
        readme += f"## Input data\n"
        readme += f"- Number of processes: {testCase.getProcessesCount()}\n"
        readme += f"- Arrival time min-max: {testCase.getProcessArrivalRange()}\n"
        readme += f"- Duration time min-max: {testCase.getProcessDurationRange()}\n\n"

        # Dla każdego algorytmu
        for testResult in testResults:
            readme += f"## Algorithm {testResult.algoShortcut}\n"

            # Dane wyjściowe
            readme += f"- Process waiting times: {testResult.getWaitingTimes()}\n"
            readme += f"- Average waiting time: {testResult.getAvgWaitingTime()}\n"

            # Wykres
            readme += f"![Graph {testResult.algoShortcut}]({testResult.algoShortcut}_{testCase.getID()}.png)\n\n"

        # Podsumowanie
        readme += f"## Summary\n\n"
        readme += f"=== REPLACE THIS WITH SUMMARY ===\n\n"

        FileManager.writeFile(path, f"{testCaseId}.md", readme)

    @staticmethod
    def generateMemoryReadme(path: str, testCaseId: int, testsManager: TestsManager):
        
        # Struktura
        # - Nazwa testu
        # - Opis testu
        # - Dane wejściowe
        # - Dla każdego algorytmu:
        #   - Dane wyjściowe
        #   - Wykresy
        #   - Opis
        # - Podsumowanie dla wszystkich algorytmów

        # Back to previous readme href
        readme = "[Back to summary](./readme.md)\n\n"

        testCase = testsManager.getMemoryTestById(testCaseId)
        testResults = testsManager.getMemoryTestResultsById(testCaseId)

        # Nazwa testu
        readme += f"# Test {testCase.testName}\n"

        # Opis testu
        readme += f"## Test description\n"
        readme += f"{testCase.testDescription}\n"
        
        # Dane wejściowe
        readme += f"## Input data\n"
        readme += f"- Memory size: {testCase.getMemorySize()}\n"
        readme += f"- Number of unique pages: {testCase.getUniuqePagesCount()}\n"
        readme += f"- Queue: {testCase.getPageAccessQueue()}\n\n"

        # Dla każdego algorytmu
        for testResult in testResults:
            readme += f"## Algorithm {testResult.algoShortcut}\n"

            # Dane wyjściowe
            readme += f"- Number of errors: {testResult.getErrorCounter()}\n"

            # Wykres
            readme += f"![Graph {testResult.algoShortcut}]({testResult.algoShortcut}_{testCase.getID()}.png)\n\n"

        # Podsumowanie
        readme += f"## Summary\n\n"
        readme += f"=== REPLACE THIS WITH SUMMARY ===\n\n"

        FileManager.writeFile(path, f"{testCaseId}.md", readme)