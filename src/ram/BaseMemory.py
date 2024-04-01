import abc
from src.ram.objects.Page import Page
from src.ram.objects.MemoryTestCase import MemoryTestCase
from src.ram.objects.MemoryTestResult import MemoryTestResult

class BaseMemory(abc.ABC):
    def __init__(self):
        # Aktualne dane testu
        self._currentTestId: str = ""
        # Indeks powinien odpowiadać ID strony - Dostępne strony do "użycia"
        self._avaliablePages: list[Page] = []
        # Lista kolejności dostępu do stron
        self._pageAccessQueue: list[int] = []
        # Aktualny czas
        self._currentTime: int = 0
        # Rozmiar pamięci
        self._memorySize = 0
        # ID Stron w pamięci
        self._pagesInMemory: list[int] = []
        # Licznik errorów - tj. Brak strony w pamięci gdy odwołanie do niej
        self._errorCounter = 0
        # Tablice do wyników
        self._removedPages: list[int] = []
        self._addedPages: list[int] = []
        self._memorySnapshots: list[list[int]] = []
        pass

    # Załadowanie testu
    def loadTestCase(self, testCase: MemoryTestCase) -> None:
        self.resetMemory()
        self._currentTestId = testCase.getID()
        self.setAvaliablePages(testCase.getPages())
        self.setPageAccessQueue(testCase.getPageAccessQueue())
        self.setMemorySize(testCase.getMemorySize())

    # Gettery

    # Zwracanie rozmiaru pamięci
    def getMemorySize(self) -> int:
        return self._memorySize
    
    # Zwracanie dostępnych stron do użycia
    def getAvaliablePages(self) -> list[Page]:
        return self._avaliablePages
    
    # Zwracanie obecnego czasu
    def getCurrentTime(self) -> int:
        return self._currentTime
    
    # Zwracanie obiektu strony o podanym ID
    def getPage(self, pageId: int) -> Page:
        return self._avaliablePages[pageId]
    
    # Zwracanie ilości błędów
    def getErrorCounter(self) -> int:
        return self._errorCounter

    # Zarządzanie stronami

    # Resetowanie pamięci
    def resetMemory(self) -> None:
        self._currentTime = 0
        self._avaliablePages = []
        self._memorySize = 0
        self._pagesInMemory = []
        self._pageAccessQueue = []
        self._errorCounter = 0
        self._removedPages = []
        self._addedPages = []
        self._memorySnapshots = []

    # Ustawianie rozmiaru pamięci
    def setMemorySize(self, memorySize: int) -> None:
        self._memorySize = memorySize

    # Ustawianie dostępnych stron do użycia
    def setAvaliablePages(self, pages: list[Page]) -> None:
        self._avaliablePages = pages
        self._checkErrors()

    # Ustawianie kolejki dostępu do stron
    def setPageAccessQueue(self, pageAccessQueue: list[int]) -> None:
        self._pageAccessQueue = pageAccessQueue

    # Pobieranie następnej strony z kolejki dostępu
    def _dequeueNextPageAccess(self) -> int:
        return self._pageAccessQueue.pop(0)
    
    # Sprawdzanie błędów, czy strony mają poprawne ID
    def _checkErrors(self) -> None:
        for i in range(0, len(self._avaliablePages)):
            if self._avaliablePages[i].getPageId() != i:
                raise Exception("Invalid page ID")
        try:
            self._pageAccessQueue.index(0)
            raise Exception("Page access queue contains 0")
        except ValueError:
            return

    # Abstrakcyjne metody
        
    # Pobieranie ID strony do usunięcia z pamięci
    @abc.abstractmethod
    def _getPageIDToRemoveFromMemory(self) -> int:
        pass


    # Pobieranie nazwy algorytmu
    @abc.abstractmethod
    def getName(self) -> str:
        pass

    # Uruchamianie

    # Dodawanie następnej strony do pamięci
    def _pushNextPageToMemory(self) -> None:
        # Pobranie ID następnej strony
        nextPageId = self._dequeueNextPageAccess()

        # Jeżeli strona jest już w pamięci
        if nextPageId in self._pagesInMemory:
            # Ustaw zmiane stron na 0
            self._addedPages.append(0)
            self._removedPages.append(0)

        # Jeżeli pamięć nie jest pełna
        elif len(self._pagesInMemory) < self._memorySize:
            # Dodanie strony do pamięci
            self._pagesInMemory.append(nextPageId)
            # Ustaw dodanie strony
            self._addedPages.append(nextPageId)
            # Ustaw usunięcie strony na 0
            self._removedPages.append(0)
            # Dodaj błąd
            self._errorCounter += 1

        # Jeżeli pamięć jest pełna + Strony nie ma w pamięci
        else:
            # Pobierz ID strony do usunięcia
            pageIdToRemove = self._getPageIDToRemoveFromMemory()
            # Pobierz indeks strony do usunięcia
            pageToRemoveIndex = self._pagesInMemory.index(pageIdToRemove)
            # Zresetuj dane usuwanej strony
            self._avaliablePages[pageIdToRemove].resetPage()
            # Dodanie strony do pamięci
            self._pagesInMemory[pageToRemoveIndex] = nextPageId
            # Dodaj błąd
            self._errorCounter += 1
            # Ustaw dodanie strony
            self._addedPages.append(nextPageId)
            # Ustaw usunięcie strony
            self._removedPages.append(pageIdToRemove)
        
        # Użyj strony - zaktualizuj dane strony
        self.getPage(nextPageId).usePage(self._currentTime)

    # Uruchomienie symulacji
    def runSimulation(self) -> None:
        # Dopóki kolejka dostępu nie jest pusta
        while len(self._pageAccessQueue) > 0:
            # Dodaj następną stronę do pamięci
            self._pushNextPageToMemory()
            # Zapisz stan pamięci
            self._memorySnapshots.append(self._pagesInMemory.copy())
            # Zwiększ czas
            self._currentTime += 1

    # Zwróc wynik symulacji
    def getResult(self) -> str:
        rawdata = "" + str(self._errorCounter) + "\n" + ' '.join(list(map(str, self._addedPages))) + "\n" + ' '.join(list(map(str, self._removedPages))) + "\n" + '\n'.join(list(map(lambda x: ' '.join(list(map(str, x))), self._memorySnapshots)))
        return MemoryTestResult(self._currentTestId, self.getName(), rawdata)