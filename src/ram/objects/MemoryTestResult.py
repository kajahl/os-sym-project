from src.objects.ATestResult import ATestResult

class MemoryTestResult(ATestResult):
    def __init__(self, testId: str, alboShortcut: str, rawData: str):
        super().__init__(testId, alboShortcut)
        lines = rawData.split("\n")
        # Rozmiar ilość błędów stron
        self.errorCounter = int(lines[0])
        # Historia zmian stron
        self.pagesChangeIn = list(map(lambda x: int(x), lines[1].split(" ")))
        self.pagesChangeOut = list(map(lambda x: int(x), lines[2].split(" ")))
        # Historia stanów pamięci
        self.memoryStates = list(map(lambda x: list(map(lambda y: int(y), x.split(" "))), lines[3:]))

    # Zwrócenie ogólnej ilości błędów
    def getErrorCounter(self) -> int:
        return self.errorCounter
    
    # Zwrócenie ID strony, która w danym momencie była ładowana do pamięci (0 = brak zmiany)
    def getPageChangeIn(self, at: int) -> list:
        return self.pagesChangeIn[at]
    
    # Zwrócenie ID strony, która w danym momencie była usuwana z pamięci (0 = brak zmiany)
    def getPageChangeOut(self, at: int) -> list:
        return self.pagesChangeOut[at]
    
    # Zwrócenie ilości stanów pamięci
    def getMemoryStatesCount(self) -> list:
        return len(self.memoryStates)

    # Zwrócenie stanu pamięci w danym momencie
    def getMemoryState(self, at: int) -> list:
        return self.memoryStates[at]
    
    # Zwrócenie ID stron które były ładowane/usuwane z pamięci w danym momencie (0 = brak zmiany)
    def getPageChangeTotal(self, at: int) -> list:
        return [self.getPageChangeIn(at), self.getPageChangeOut(at)]
    
    def __str__(self) -> str:
        # rawdata = "" + str(self._errorCounter) + "\n" + ' '.join(list(map(str, self._addedPages))) + "\n" + ' '.join(list(map(str, self._removedPages))) + "\n" + '\n'.join(list(map(lambda x: ' '.join(list(map(str, x))), self._memorySnapshots)))
        # return ' '.join(list(map(str, self._executingTimeline))) + "\n" + ' '.join(list(map(str, [process.getTotalWaitingTime() for process in self._processes]))) + "\n" + str(sum([process.getTotalWaitingTime() for process in self._processes])/len(self._processes))
        return "" + str(self.errorCounter) + "\n" + ' '.join(list(map(str, self.pagesChangeIn))) + "\n" + ' '.join(list(map(str, self.pagesChangeOut))) + "\n" + '\n'.join(list(map(lambda x: ' '.join(list(map(str, x))), self.memoryStates)))