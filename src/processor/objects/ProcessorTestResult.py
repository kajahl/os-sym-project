from src.objects.ATestResult import ATestResult

class ProcessorTestResult(ATestResult):
    def __init__(self, testId: str, alboShortcut: str, rawData: str):
        super().__init__(testId, alboShortcut)
        lines = rawData.split("\n")
        # Zapisanie osi czasu
        self._timeline = [int(x) for x in lines[0].split(" ")]
        # Zapisanie czasów oczekiwania
        self._waitingTimes = [int(x) for x in lines[1].split(" ")]

    # Zwrócenie listy ID procesów w kolejności ich wykonywania
    def getTimeline(self) -> list[int]:
        return [p for p in self._timeline]
    
    # Zwrócenie listy czasów oczekiwania procesów
    def getWaitingTimes(self) -> list[int]:
        return [p for p in self._waitingTimes]
    
    # Zwrócenie średniego czasu oczekiwania
    def getAvgWaitingTime(self) -> float:
        return sum(self._waitingTimes) / len(self._waitingTimes)
    
    # Zwrócenie średniego czasu oczekiwania
    def getProcessWaitingTime(self, processId: int) -> int:
        return self._waitingTimes[processId]

    # Zwrócenie czasu, w którym proces zaczął się wykonywać
    def getProcessExecutingStartTime(self, processId: int) -> int:
        return self._timeline.index(processId)
    
    # Zwrócenie czasu, w którym proces skończył się wykonywać
    def getProcessExecutingEndTime(self, processId: int) -> int:
        return len(self._timeline) - self._timeline[::-1].index(processId)
    
    def __str__(self) -> str:
        # return ' '.join(list(map(str, self._executingTimeline))) + "\n" + ' '.join(list(map(str, [process.getTotalWaitingTime() for process in self._processes]))) + "\n" + str(sum([process.getTotalWaitingTime() for process in self._processes])/len(self._processes))
        return ' '.join(list(map(str, self._timeline))) + "\n" + ' '.join(list(map(str, self._waitingTimes))) + "\n" + str(sum(self._waitingTimes)/len(self._waitingTimes))