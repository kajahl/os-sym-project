class Page():
    def __init__(self, pageId):
        # PID - Identyfikator
        self.pageId = pageId
        # Licznik użycia - Jeżeli w pamięci
        self.pageUsageCounter = 0
        # Czas ostatniego użycia - Jeżeli w pamięci
        self.lastUsedTimestamp = 0
        # Czas dodania do pamięci
        self.addedTimestamp = -1

    # Zwracanie ID strony
    def getPageId(self):
        return self.pageId
    
    # Zwracanie licznika użycia strony
    def getPageUsageCounter(self):
        return self.pageUsageCounter
    
    # Zwracanie czasu ostatniego użycia strony
    def getLastUsedTimestamp(self):
        return self.lastUsedTimestamp
    
    # Zwracanie czasu dodania strony do pamięci
    def getAddedTimestamp(self):
        return self.addedTimestamp
    
    # Użycie strony - zarządzanie danymi strony (dodanie, ostatnie użycie, ilość użyć)
    def usePage(self, time):
        # Dodanie użycia strony
        self.pageUsageCounter += 1
        # Ustawienie ostatniego użycia
        self.lastUsedTimestamp = time
        # Jeżeli strona nie była jeszcze dodana do pamięci - ustawienie czasu dodania
        if self.addedTimestamp == -1:
            self.addedTimestamp = time

    # Reset strony - ustawienie licznika użycia na 0, czasu ostatniego użycia na 0, czasu dodania na -1
    def resetPage(self):
        self.pageUsageCounter = 0
        self.lastUsedTimestamp = 0
        self.addedTimestamp = -1