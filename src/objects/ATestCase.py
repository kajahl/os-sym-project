from abc import ABC, abstractmethod

# Abstrakcyjna klasa do ewentualnych wspólnych cech testów
class ATestCase(ABC):
    def __init__(self, fileName: str):
        self.fileName = fileName

    @abstractmethod
    def getID(self) -> str:
        pass