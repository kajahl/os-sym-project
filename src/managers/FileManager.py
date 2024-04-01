import os

class FileManager():
    # Ścieżki i nazwy do odpowiednich folderów
    __input_path = os.path.join(os.getcwd(), "input")
    __output_path = os.path.join(os.getcwd(), "output")
    __processor_folder_name = "processor_tests"
    __memory_folder_name = "memory_tests"


    # Tworzenie folderów gdy nie istnieją
    @staticmethod
    def createRequiredFolders() -> None:
        requiredFolders = [
            FileManager.getInputPath(),
            FileManager.getOutputPath(),
            FileManager.joinPath(FileManager.getInputPath(), FileManager.getProcessorFolderName()),
            FileManager.joinPath(FileManager.getInputPath(), FileManager.getMemoryFolderName()),
            FileManager.joinPath(FileManager.getOutputPath(), FileManager.getProcessorFolderName()),
            FileManager.joinPath(FileManager.getOutputPath(), FileManager.getMemoryFolderName())
        ]
        for folder in requiredFolders:
            if not os.path.exists(folder):
                os.makedirs(folder)

    # Ogólne metody

    # Ścieżka do folderu z plikami wejściowymi
    @staticmethod
    def getInputPath() -> str:
        return FileManager.__input_path
    
    # Ścieżka do folderu z plikami wyjściowymi
    @staticmethod
    def getOutputPath() -> str:
        return FileManager.__output_path
    
    # Nazwa folderu definiowanego dla procesora
    @staticmethod
    def getProcessorFolderName() -> str:
        return FileManager.__processor_folder_name
    
    # Nazwa folderu definiowanego dla pamięci
    @staticmethod
    def getMemoryFolderName() -> str:
        return FileManager.__memory_folder_name
    
    # Łączenie ścieżek
    @staticmethod
    def joinPath(*args) -> str:
        return os.path.join(*args)

    # Pobierz nazwy plików z folderu
    @staticmethod
    def getFiles(path: str, ext: str = "txt") -> list[str]:
        return os.listdir(path) if ext == "" else [file for file in os.listdir(path) if file.endswith(ext)]

    # Sprawdzenie czy plik istnieje w folderze
    @staticmethod
    def isFile(path: str, filename: str) -> bool:
        return os.path.isfile(os.path.join(path, filename))

    # Odczytanie zawartści pliku
    @staticmethod
    def readFile(path: str, filename: str) -> list[str]:
        fullPath = os.path.join(path, filename)
        # Jeżeli plik nie istnieje - zwróć wyjątek
        if not FileManager.isFile(path, filename):
            raise Exception(f"File {fullPath} does not exist")
        # Odczytaj plik
        with open(fullPath, 'r', encoding="UTF8") as plik:
            content = plik.read()
        return content
    
    # Zapisanie zawartści pliku
    @staticmethod
    def writeFile(path: str, filename: str, content: str) -> None:
        fullPath = os.path.join(path, filename)
        # Jeżeli nie istnieje folder - utwórz
        if not os.path.exists(path):
            os.makedirs(path)
        # Zapisz plik
        with open(fullPath, 'w', encoding="UTF8") as plik:
            plik.write(content)
        return None

    # Metody szczególne

    # Zwrócenie listy plików z folderu z testami dla procesora
    @staticmethod
    def getProcessorTests() -> list[str]:
        return FileManager.getFiles(FileManager.joinPath(FileManager.getInputPath(), FileManager.getProcessorFolderName()), "txt")
    
    # Zwrócenie listy plików z folderu z testami dla pamięci
    @staticmethod
    def getMemoryTests() -> list[str]:
        return FileManager.getFiles(FileManager.joinPath(FileManager.getInputPath(), FileManager.getMemoryFolderName()), "txt")
    
    # Zwrócenie listy plików z folderu z wynikami dla procesora
    @staticmethod
    def getProcessorTestsResults() -> list[str]:
        return FileManager.getFiles(FileManager.joinPath(FileManager.getOutputPath(), FileManager.getProcessorFolderName()), "txt") 
    
    # Zwrócenie listy plików z folderu z wynikami dla pamięci
    @staticmethod
    def getMemoryTestsResults() -> list[str]:
        return FileManager.getFiles(FileManager.joinPath(FileManager.getOutputPath(), FileManager.getMemoryFolderName()), "txt")
    
    # Usunięcie komentarzy z pliku
    @staticmethod
    def removeComments(rawData: str) -> str:
        lines = rawData.split("\n")
        newRawData = []
        for line in lines:
            if line.startswith("#"):
                continue
            if len(line) == 0:
                continue
            indexOfComment = line.find("#")
            if indexOfComment != -1:
                line = line[:indexOfComment]
            newRawData.append(line)
        return "\n".join(newRawData)