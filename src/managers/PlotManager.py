from matplotlib import pyplot as plt
from abc import ABC
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

from src.managers.FileManager import FileManager
from src.processor.objects.ProcessorTestCase import ProcessorTestCase
from src.processor.objects.ProcessorTestResult import ProcessorTestResult
from src.ram.objects.MemoryTestCase import MemoryTestCase
from src.ram.objects.MemoryTestResult import MemoryTestResult

class PlotManager(ABC):
    # Zwrócenie legendy dla osi czasu procesora
    @staticmethod
    def getProcessorTimelineLegend(withMarkers: bool = True):
        legend = []
        if withMarkers: legend.append(plt.Line2D([0], [0], marker='^', linestyle='', color='green', label='Coming', markersize=6))
        legend.append(plt.Line2D([0], [0], color='green', linestyle=':', label='Waiting'))
        if withMarkers: legend.append(plt.Line2D([0], [0], marker='o', linestyle='', color='blue', label='Started', markersize=6))
        legend.append(plt.Line2D([0], [0], color='black', linestyle='solid', label='Executing'))
        if withMarkers: legend.append(plt.Line2D([0], [0], marker='o', linestyle='', color='red', label='Ended', markersize=6))
        return legend

    # Zwrócenie legendy dla osi czasu pamięci
    @staticmethod
    def getMemoryTimelineLegend():
        legend_elements = [
            mpatches.Patch(color='green', label='Adding to memory'),
            mpatches.Patch(color='cyan', label='Page Usage'),
            mpatches.Patch(color='red', label='Deleting from memory'),
        ]
        return legend_elements

    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self._width = 0
        self._height = 0
        self._min_tick_x = 1
    
    # Ustawienie rozmiaru
    def setSize(self, width, height):
        self._width = width
        self._height = height
        return self
    
    # Ustawienie szerokości
    def setWidth(self, width):
        self._width = width
        return self
    
    # Ustawienie wysokości
    def setHeight(self, height):
        self._height = height
        return self
    
    # Ustawienie opisu osi X
    def setXLabel(self, label):
        self.ax.set_xlabel(label)
        return self
    
    # Ustawienie opisu osi Y
    def setYLabel(self, label):
        self.ax.set_ylabel(label)
        return self
    
    # Ustawienie tytułu
    def setTitle(self, title):
        self.ax.set_title(title)
        return self
    
    # Rysowanie siatki
    def setXGrid(self, minTick):
        for i in range(0, self._width+1):
            if i % minTick == 0:
                for j in range(0, self._height):
                    self.ax.vlines(i, j, j+1, colors='gray', linestyles='dashed', linewidth=0.5)
        return self
    
    # Rysowanie siatki
    def setYGrid(self, minTick):
        for i in range(0, self._height+1):
            if i % minTick == 0:
                for j in range(0, self._width):
                    self.ax.hlines(i, j, j+1, colors='gray', linestyles='dashed', linewidth=0.5)
        return self
    
    # Sprawdzenie poprawności danych
    def __checkRange(self, second: int, value: int):
        if second < 0:
            raise ValueError("Second must be greater than 0")
        if second > self._width:
            raise ValueError("Second must be less than graph width (max X axis)")
        if value < 0:
            raise ValueError("Value must be positive")
        if value > self._height:
            raise ValueError("Value must be less than graph height (max Y axis)")
    
    # Rysowanie linii
    def drawLine(self, second: int, value: int, color: str = 'black', style: str = 'solid'):
        self.__checkRange(second, value)
        self.ax.plot([second, second+1], [value, value], color=color, linestyle=style)
        return self
    
    # Rysowanie znacznika
    def drawMark(self, second: int, value: int, type: str = 'o', color: str = 'black', endOfSecond: bool = True):
        self.__checkRange(second, value)
        self.ax.plot(second if endOfSecond else second - 1, value, color=color, marker=type)
        return self
    
    # Rysowanie prostokąta
    def drawRect(self, second: int, value: int, color: str = 'black', width: float = 1):
        self.__checkRange(second, value)
        self.ax.add_patch(Rectangle((second, value), width, -1, color=color))
        return self
    
    # Dodanie legendy
    def addLegend(self, legend):
        plt.legend(handles=legend)

    # Wyświetlenie wykresu
    def show(self):
        bottomMargin = 1
        self.ax.set_xlim(-1, self._width + 1)
        self.ax.set_ylim(-1 * bottomMargin, self._height)
        plt.xticks(np.arange(0, self._width + 1, self._min_tick_x))
        for i in range(0, self._width):
            self.ax.hlines(i, 0, self._width, colors='gray', linestyles='dashed', linewidth=0.5)
        plt.show()
        return self
    
    # Dodanie tekstu
    def addText(self, x: int, y: int, text: str, color: str = 'black', size: int = 10):
        self.ax.text(x, y, text, color=color, size=size)
        return self
    
    # Zapisanie wykresu
    def saveAt(self, fullpath: str):
        plt.savefig(fullpath)
        plt.close(self.fig)

    @staticmethod
    # Wygenerowanie wykresu dla procesora
    def makeProcessorGraph(testCase: ProcessorTestCase, results: ProcessorTestResult):
        if testCase is None:
            print(f"Brak danych do wygenerowania wykresu (Brak zdefiniowanego testu procesora dla {results.getOutputFileName()})")
            return

        print(f"Tworzenie wykresu dla {results.getOutputFileName()}")

        # Tworzenie wykresu i ustawianie podstawowych wartości
        graph = PlotManager()
        width = len(results.getTimeline())
        height = testCase.getProcessesCount() - 1
        graph.setSize(width, height)
        graph.setTitle(f"{results.algoShortcut} - {testCase.testName}")
        graph.setXLabel("Time")
        graph.setYLabel("Process ID")
        graph.setXGrid(width // 10 if width > 10 else 1)
        graph.setYGrid(height // 10 if height > 10 else 1)
        canDrawMarkers = width < 50

        # Rysowanie wykonania procesów w czasie
        for i in range(len(results.getTimeline())):
            if i == -1:
                continue
            graph.drawLine(i, results.getTimeline()[i])

        # Zaznaczanie momentów ma wykresach
        for process in testCase.getProcesses():
            start = results.getProcessExecutingStartTime(process.getProcessId())
            end = results.getProcessExecutingEndTime(process.getProcessId())

            # Zaznaczanie oczekiwania
            for i in range(process.getProcessArrival(), start):
                graph.drawLine(i, process.getProcessId(), color='green', style=':')

            # Dodanie znaczników
            if canDrawMarkers:
                # Przybycie procesu
                graph.drawMark(process.getProcessArrival(), process.getProcessId(), type='^', color='green')
                # Rozpoczęcie wykonywania procesu
                graph.drawMark(start, process.getProcessId(), type='o', color='blue')
                # Zakończenie wykonywania procesu
                graph.drawMark(end, process.getProcessId(), type='o', color='red')

        # Dodanie legendy
        graph.addLegend(PlotManager.getProcessorTimelineLegend(canDrawMarkers))

        # Zapis wykresu
        fullPath = FileManager.joinPath(FileManager.getOutputPath(), FileManager.getProcessorFolderName(), results.getOutputFileName().replace(".txt", ".png"))
        graph.saveAt(fullPath)
        # print(f"Zapisano wykres w folderze {fullPath}")
        return

    @staticmethod
    def makeMemoryGraph(testCase: MemoryTestCase, results: MemoryTestResult):
        if testCase is None:
            print(f"Brak danych do wygenerowania wykresu (Brak zdefiniowanego testu memory dla {results.getOutputFileName()})")
            return

        print(f"Tworzenie wykresu dla {results.getOutputFileName()}")

        # Tworzenie wykresu i ustawianie podstawowych wartości
        graph = PlotManager()
        width = results.getMemoryStatesCount()
        height = testCase.getUniuqePagesCount()
        height += (height//5 + 1)
        graph.setSize(width, height)
        graph.setTitle(f"{results.algoShortcut} - {testCase.testName}")
        graph.setXLabel("Time")
        graph.setYLabel("Page ID")

        # Dodanie linii siatki co 1 jednostkę
        graph.setXGrid(1)
        graph.setYGrid(1)

        # Rysowanie stanów pamięci w czasie
        for i in range(results.getMemoryStatesCount()):
            # Pobranie stanu pamięci w danym momencie
            memoryState = results.getMemoryState(i)
            # Zaznaczenie, które strony były załadowane
            for y in range(len(memoryState)):
                graph.drawRect(i, memoryState[y])
            # Zaznaczenie żądań do stron pamięci
            pageUsed = testCase.getPageAccessQueue()[i]
            graph.drawRect(i, pageUsed, color='cyan')
            # Zaznaczenie zmian stron
            markSize = 0.25
            pageIn = results.getPageChangeIn(i)
            pageOut = results.getPageChangeOut(i)
            if pageIn != 0: graph.drawRect(i, pageIn, color='green', width=markSize)
            if pageOut != 0: graph.drawRect(i, pageOut, color='red', width=-markSize)

        # Dodanie legendy
        graph.addLegend(PlotManager.getMemoryTimelineLegend())

        # Zapis wykresu
        fullPath = FileManager.joinPath(FileManager.getOutputPath(), FileManager.getMemoryFolderName(), results.getOutputFileName().replace(".txt", ".png"))
        graph.saveAt(fullPath)
        return