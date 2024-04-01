class Process():
    def __init__(self, processId, processArrival, processDuration):
        # Readonly - dane podstawowe
        self.__processId : int = processId
        self.__processArrival : int = processArrival
        self.__processDuration : int = processDuration
        # Dane dynamiczne - zmieniające się w trakcie działania programu
        self._lastTimeExecuted : int = processArrival
        self._totalWaitingTime : int = 0
        self._totalExecutionTime : int = 0
        self._executedAtTimestamps : list[int] = []

    # Gettery do danych podstawowych
        
    # Zwrócenie ID procesu
    def getProcessId(self) -> int:
        return self.__processId
    
    # Zwrócenie czasu przyjścia procesu
    def getProcessArrival(self) -> int:
        return self.__processArrival
    
    # Zwrócenie czasu trwania procesu
    def getProcessDuration(self) -> int:
        return self.__processDuration
    
    # Metody do danych dynamicznych

    # Zwrócenie całkowitego czasu wykonania procesu
    def getTotalExecutionTime(self) -> int:
        return self._totalExecutionTime
    
    # Zwrócenie całkowitego czasu oczekiwania procesu
    def getTotalWaitingTime(self) -> int:
        return self._totalWaitingTime
    
    # Zwrócenie czasu ostatniego wykonania procesu
    def getLastTimeExecuted(self) -> int:
        return self._lastTimeExecuted
    
    # Zwrócenie listy czasów wykonania procesu
    def getExecutedAtTimestamps(self) -> list[int]:
        return self._executedAtTimestamps
    
    # Wykonwanie procesu w czasie
    def executeProcess(self, time) -> None:
        # Czas od ostatniego wywołania
        timeFromLastExecution = time - self._lastTimeExecuted
        # Dodanie czasu oczekiwania do sumy (jeżeli czas oczekiwania jest większy od 0*)
        self._totalWaitingTime += (timeFromLastExecution if timeFromLastExecution > 0 else 0)
        # Log 
        # if(timeFromLastExecution > 0):
        #     print(f"PID [{self.__processId}] executed at [{time}s] was waiting for [{timeFromLastExecution}s] from [{self._lastTimeExecuted}s] to [{time}s]. Total waiting time: [{self._totalWaitingTime}s]")
        # else:
        #     print(f"PID [{self.__processId}] executed at [{time}s]. (Skipped waiting time: {timeFromLastExecution}) Total waiting time: [{self._totalWaitingTime}s]")
        # Zapisanie czasu ostatniego wykonania (+1, bo proces wykonuje się w tym momencie - np.: Wykonywanie W PIĄTEJ SEKUNDZIE, więc skończy się wykonywać na początku szóstej)
        self._lastTimeExecuted = time + 1
        # Zwiększenie całkowitego czasu wykonania
        self._totalExecutionTime += 1
        # Dodanie czasu wykonania do listy
        self._executedAtTimestamps.append(time)

    # Sprawdzenie czy proces wykonał się w całości
    def isProcessDone(self) -> bool:
        return self._totalExecutionTime == self.__processDuration
    
    # Sprawdzenie czy proces już przyszedł
    def isProcessCame(self, time) -> bool:
        return self.__processArrival <= time
    