from src.processor.BaseProcessor import BaseProcessor

class FCFSProcessor(BaseProcessor):
    def __init__(self):
        super().__init__()

    # Zwrócenie nazwy procesora
    def getName(self) -> str:
        return "FCFS"

    # Zwrócenie ID procesu, który powinien zostać wykonany
    def _getNextProcessId(self) -> int:
        # Pobranie listy procesów, które są dostępne do wykonania
        processes = self.getAvalibleProcesses()
        # Sortowanie procesów według czasu przybycia (Rosnąco) - po tym będzie wybierany proces
        processes.sort(key=lambda process: process.getProcessArrival())
        # Jeżeli brak - zwróć -1
        if len(processes) == 0:
            return -1
        # Pobranie najniższego czasu przybycia
        timeArrival = processes[0].getProcessArrival()
        # Pobranie procesów, które mają najniższy czas przybycia
        processes = [process for process in processes if process.getProcessArrival() == timeArrival]
        # Jeżeli jest ich więcej niż jeden - posortuj po ID
        processes.sort(key=lambda process: process.getProcessId())
        # Zwróć ID procesu do wykonania
        return processes[0].getProcessId()