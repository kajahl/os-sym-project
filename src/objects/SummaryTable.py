import pandas as pd

# SummaryCell to przechowalnia dla pojedynczej komórki
class SummaryCell:
    def __init__(self, row, column, value) -> None:
        self.value: str = value
        self.row: str = row
        self.column: str = column
        return

# SummaryTable klasa tworząca tabele podsumowującą
class SummaryTable:
    def __init__(self) -> None:
        self.columns: list[str] = []
        self.rows: list[str] = []
        self.values: list[SummaryCell] = []
        return

    # Ustawienie kolumn
    def setColumns(self, columns: list[str]) -> None:
        self.columns = columns

    # Ustawienie wierszy
    def setRows(self, rows: list[str]) -> None:
        self.rows = rows

    # Ustawienie wartości
    def setValue(self, column: str, row: str, value: str) -> None:
        if column not in self.columns:
            # print(column, self.columns)
            raise Exception(f"Column {column} not found")
        if row not in self.rows:
            # print(row, self.rows)
            raise Exception(f"Row {row} not found")
        self.values.append(SummaryCell(column, row, value))

    # Ustawienie wartości dla całej tabeli
    def fillValues(self, value: str) -> None:
        for value in self.values:
            value.value = value

    # Wypisanie wartości
    def printValues(self) -> None:
        for value in self.values:
            print(f"{value.column} {value.row} {value.value}")

    # Pobranie wartości
    def getValue(self, row: str, column: str) -> str:
        for value in self.values:
            if value.column == column and value.row == row:
                return value.value
        raise Exception(f"Value for column {column} and row {row} not found")

    # Pobranie tabeli
    def getTable(self) -> pd.DataFrame:
        values = [[self.getValue(self.columns[x], self.rows[y]) for x in range(len(self.columns))] for y in range(len(self.rows))]
        return pd.DataFrame(values, index=self.rows, columns=self.columns)