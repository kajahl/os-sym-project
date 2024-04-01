from src.processor.objects.Process import Process
from src.processor.objects.ProcessorTestCase import ProcessorTestCase
import random

# Klasa generująca procesy
class ProcessGenerator:
    def __init__(self):
        self.processes = []

    # Generowanie procesów na podstawie podanych parametrów - count: ilość, przedział czasu przyjścia, przedział czasu trwania
    def generateProcesses(self, count: int, minTimeArrival: int = 1, maxTimeArrival: int = None, minTimeDuration: int = 1, maxTimeDuration: int = 10):
        # Ustawienie maksymalnego czasu przyjścia na podstawie minimalnego czasu trwania - jeżeli nie ustawione
        if maxTimeArrival is None:
            maxTimeArrival = count * minTimeDuration
        # Generowanie count procesów
        for _ in range(count):
            process = Process(0, random.randint(minTimeArrival, maxTimeArrival), random.randint(minTimeDuration, maxTimeDuration))
            self.processes.append(process)
        return self

    # Zwrócenie listy procesów
    def get(self):
        return self.processes
    
    # Sortowanie procesów po czasie przyjścia
    def sort(self):
        self.processes.sort(key=lambda x: x.getProcessArrival())
        return self
    
    # Wyczyszczenie listy procesów
    def clear(self):
        self.processes = []

    # Zapisanie testu do pliku
    def saveTestCase(self, fileName: str, testName: str, testDescription: str):
        ProcessorTestCase.create(fileName, testName, testDescription, self.processes)