from src.ram.objects.MemoryTestCase import MemoryTestCase
import random

# Klasa generująca kolejki dostępu do stron
class QueueGenerator:
    def __init__(self, memorySize, uniquePagesSize) -> None:
        self.queue : list[int] = []
        # memorySize - rozmiar pamięci
        self.memorySize = memorySize
        # uniquePagesSize - ilość unikalnych stron
        self.uniquePagesSize = uniquePagesSize

    # Generowanie kolejki o zadanej długości (queueSize), z prawdopodobieństwem powtórzenia poprzedniej wartości (nextSamePageProbability), maksymalna ilość powtórzonych stron dla dodatkowego prawdopodobieństwa (maxSamePageCount), ID z zakresu [pageMin, pageMax]
    def generateQueue(self, queueSize: int, nextSamePageProbability: float = None, maxSamePageCount: int = None, pageMin: int = 1, pageMax: int = None):

        # Ustawienie danych domyślnych i sprawdzenie warunków
        nextSamePageProbability = 1/self.uniquePagesSize if nextSamePageProbability == None else nextSamePageProbability
        maxSamePageCount = queueSize if maxSamePageCount == None else maxSamePageCount
        pageMax = self.uniquePagesSize if pageMax == None else pageMax
        if pageMin > pageMax:
            raise Exception("pageMin > pageMax")
        if self.uniquePagesSize < pageMax:
            raise Exception("pageCount < pageMax")
        if pageMin < 1:
            raise Exception("pageMin < 1")
        
        # Generowanie kolejki
        for i in range(queueSize):
            # Sprawdzenie czy kolejna strona może być taka sama - if(True) = Losowanie kolejnej strony bez dodatkowego prawdopodobieństwa
            # len(self.queue) >= maxSamePageCount - sprawdzenie czy istnieje wystarczająca ilość stron do sprawdzenia, czy został osiągnięty max powtórzeń
            # sum(self.queue[-maxSamePageCount:]) == self.queue[-1] * maxSamePageCount - sprawdzenie czy ostatnie maxSamePageCount stron są takie same
            if len(self.queue) >= maxSamePageCount and sum(self.queue[-maxSamePageCount:]) == self.queue[-1] * maxSamePageCount:
                nextRandom = random.randint(pageMin, pageMax)
                while nextRandom == self.queue[-1]:
                    nextRandom = random.randint(pageMin, pageMax)
                self.queue.append(nextRandom)
                continue
            # Sprawdzenie czy kolejna strona ma być taka sama
            if random.random() < nextSamePageProbability and len(self.queue) > 0:
                self.queue.append(self.queue[-1])
                continue
            # Losowanie kolejnej strony
            self.queue.append(random.randint(pageMin, pageMax))
        return self

    # Dodawanie stron do kolejki - bez generatora - dodawanie stron z listy
    def add(self, pages: int):
        for page in pages:
            # Sprawdzenie czy strona spełnia warunki określone w konstruktorze
            if page > self.uniquePagesSize:
                raise Exception("page > uniquePagesSize")
            if page < 1:
                raise Exception("page < 1")
            # Dodanie pamięci
            self.queue.append(page)
        return self

    # Dodawanie stron do kolejki - bez generatora - dodawanie stron z listy na określonej pozycji
    def insert(self, index: int, pages: int):
        for page in pages:
            # Sprawdzenie czy strona spełnia warunki określone w konstruktorze
            if page > self.uniquePagesSize:
                raise Exception("page > uniquePagesSize")
            if page < 1:
                raise Exception("page < 1")
            # Dodanie pamięci
            self.queue.insert(index, page)
            index += 1
        return self

    # Zwrócenie kolejki
    def get(self):
        return self.queue
    
    # Wyczyszczenie kolejki
    def clear(self):
        self.queue = []

    # Zapisywanie testu do pliku
    def saveTestCase(self, fileName: str, testName: str, testDescription: str):
        MemoryTestCase.create(fileName, testName, f"{testDescription} [Rozmiar pamięci: {self.memorySize}, Unikalne strony: {self.uniquePagesSize}, Długość kolejki: {len(self.queue)}]", self.memorySize, self.queue)