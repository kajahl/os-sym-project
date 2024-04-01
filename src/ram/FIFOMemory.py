from src.ram.BaseMemory import BaseMemory

# FIFO - First In First Out
class FIFOMemory(BaseMemory):
    def __init__(self):
        super().__init__()
        return

    # Zwróć nazwę algorytmu
    def getName(self) -> str:
        return "FIFO"
    
    # Zwróć ID Strony do usunięcia
    def _getPageIDToRemoveFromMemory(self) -> int:
        # Pobranie obiektów wszystkich stron w pamięci
        pagesInMemory = [self.getPage(pageId) for pageId in self._pagesInMemory]
        # Pobranie czasów dodania stron do pamięci - według tego czasu będzie wybierana strona do usunięcia
        pagesTimestamps = [page.getAddedTimestamp() for page in pagesInMemory]
        # Znalezienie najstarszego czasu dodania strony do pamięci
        oldestAddTimestamp = min(pagesTimestamps)
        # ^ Jeżeli ta funkcja jest wywoływana, to znaczy że w pamięć powinna być pełna. Jeżeli min = -1 => Błąd
        if oldestAddTimestamp == -1:
            raise Exception("Error while removing page from memory")
        # Pobranie ID strony do usunięcia
        pageIdToRemove = [page.getPageId() for page in pagesInMemory if page.getAddedTimestamp() == oldestAddTimestamp][0]
        return pageIdToRemove
