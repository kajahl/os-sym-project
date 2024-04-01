from abc import ABC, abstractmethod

# Abstrakcyjna klasa do ewentualnych wspólnych cech testów
class ATestResult(ABC):
    def __init__(self, testId: str, alboShortcut: str):
        self.testId = testId
        self.algoShortcut = alboShortcut

    def getOutputFileName(self) -> str:
        return f"{self.algoShortcut}_{self.testId}.txt"