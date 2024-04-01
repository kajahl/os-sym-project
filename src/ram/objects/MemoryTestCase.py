from src.ram.objects.Page import Page
from src.objects.ATestCase import ATestCase
from src.managers.FileManager import FileManager
import numpy as np

# Klasa reprezentująca test pamięci
class MemoryTestCase(ATestCase):
    def __init__(self, fileName: str, rawData: str):
        super().__init__(fileName)
        lines = rawData.split("\n")
        # ID
        self._id = lines[0]
        # Nazwa testu
        self.testName = lines[1]
        # Opis testu
        self.testDescription = lines[2]
        # Rozmiar pamięci
        self.testMemorySize = int(lines[3])
        # Kolejność dostępu do stron
        self.testPageAccessQueue = [int(pageId) for pageId in lines[4].split(" ")]
        # Ilość stron - maksymalna wartość z kolejki dostępu
        self.testPages = max(self.testPageAccessQueue)

    # Zwróć ID
    def getID(self) -> str:
        return self._id

    # Zwracanie obiektów stron do testów - strony ID z zakresu [0, testPages]
    def getPages(self) -> list[Page]:
        return [Page(pageId) for pageId in range(0, self.testPages + 1)]

    # Zwracanie kolejki dostępu do stron
    def getPageAccessQueue(self) -> list[int]:
        return [pageId for pageId in self.testPageAccessQueue]

    # Zwracanie rozmiaru pamięci
    def getMemorySize(self) -> int:
        return self.testMemorySize
    
    # Zwracanie ilości stron (unikalna ilość stron w kolejce dostępu tj. dla [1,5,3,5,3,6] => Unikalne = [1,3,5,6] => 4)
    def getUniuqePagesCount(self) -> int:
        return len(np.unique(self.getPageAccessQueue()))
    
    # Formatowanie wyniku testu
    def formatResult(self, result: str) -> str:
        return f"{result}"
    
    # Zwracanie informacji o teście
    def __str__(self) -> str:
        return f"ProcessorTest - {self.testName}\nDescription: {self.testDescription}\nMemory size: {self.testMemorySize}\nPage access queue: {self.testPageAccessQueue}\nPages count: {self.testPages}"
    
    # Zapisywanie testu do pliku
    @staticmethod
    def create(fileName: str, title: str, description: str, memorySize: int, pageAccessQueue: list[int]):
        # Stworzenie zapisu tekstowego
        content = ""
        content += f"{title}\n"
        content += f"{description}\n"
        content += f"{memorySize}\n"
        content += f"{' '.join([str(x) for x in pageAccessQueue])}\n"
        # Zapis do pliku
        fullPath = FileManager.joinPath(FileManager.getInputPath(), FileManager.getMemoryFolderName())
        FileManager.writeFile(fullPath, fileName, content)
        print(f"Utworzono test {fileName} w {fullPath}")
        