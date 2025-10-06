class Spreadsheet:

    def __init__(self, rows: int):
        # Store spreadsheet as a default dict
        self.sheet = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        # Set the given cell to a value
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        # Zero the given cell
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        # Split the formula to get both addends
        a, b = formula[1:].split("+")

        # Evaluate both as numbers and return the result
        evaluate = lambda x: int(x) if x[0].isnumeric() else self.sheet[x]
        return evaluate(a) + evaluate(b)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)