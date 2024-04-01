from src.ram.BaseMemory import BaseMemory

# LFU - Least Frequently Used
class LFUMemory(BaseMemory):
    def __init__(self):
        super().__init__()
        return
        
    # Zwróć nazwę algorytmu
    def getName(self) -> str:
        return "LFU"
    
    # Zwróć ID Strony do usunięcia
    def _getPageIDToRemoveFromMemory(self) -> int:
        # Pobranie obiektów wszystkich stron w pamięci
        pagesInMemory = [self.getPage(pageId) for pageId in self._pagesInMemory]
        # Pobranie ilości użycia stron pamięci - według tego czasu będzie wybierana strona do usunięcia
        pagesUsage = [page.getPageUsageCounter() for page in pagesInMemory]
        # Znalezienie najmniejszej ilości użycia strony
        minUsageCounter = min(pagesUsage)
        # ^ Jeżeli ta funkcja jest wywoływana, to znaczy że w pamięć powinna być pełna. Jeżeli min = -1 => Błąd
        if minUsageCounter == -1:
            raise Exception("Error while removing page from memory")
        # Pobranie ID stron (moze być więcej z tą wartością użycia) do usunięcia
        pagesWithMinUsageCounter = [page for page in pagesInMemory if page.getPageUsageCounter() == minUsageCounter]
        # Jeżeli jest więcej niż jedna strona z najmniejszym timestampem, to bierzemy tą, która została użyta wcześniej (dłużej nieużywana - jak w LFU)
        if len(pagesWithMinUsageCounter) > 1:
            pagesWithMinUsageCounter.sort(key=lambda page: page.getLastUsedTimestamp(), reverse=True)
            # Reverse=True => Malejąco. Bierzemy tą, która została użyta wcześniej (dłużej nieużywana - jak w LRU)
        # Pobranie ID strony do usunięcia
        pageIdToRemove = pagesWithMinUsageCounter[0].getPageId()
        return pageIdToRemove
