from src.ram.BaseMemory import BaseMemory

# LRU - Least Recently Used
class LRUMemory(BaseMemory):
    def __init__(self):
        super().__init__()
        return

    # Zwróć nazwę algorytmu
    def getName(self) -> str:
        return "LRU"
    
    # Zwróć ID Strony do usunięcia
    def _getPageIDToRemoveFromMemory(self) -> int:
        # Pobranie obiektów wszystkich stron w pamięci
        pagesInMemory = [self.getPage(pageId) for pageId in self._pagesInMemory]
        # Pobranie czasów ostatniego użycia stron pamięci - według tego czasu będzie wybierana strona do usunięcia
        pagesTimestamps = [page.getLastUsedTimestamp() for page in pagesInMemory]
        # Znalezienie najstarszego czasu ostatniego użycia strony
        leastRecentlyUsedTimestamp = min(pagesTimestamps)
        # ^ Jeżeli ta funkcja jest wywoływana, to znaczy że w pamięć powinna być pełna. Jeżeli min = -1 => Błąd
        if leastRecentlyUsedTimestamp == -1:
            raise Exception("Error while removing page from memory")
        # Pobranie ID strony
        pageIdToRemove = [page.getPageId() for page in pagesInMemory if page.getLastUsedTimestamp() == leastRecentlyUsedTimestamp][0]
        return pageIdToRemove
