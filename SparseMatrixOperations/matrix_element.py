class MatrixElement:
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val

    def __str__(self):
        return f"({self.row}, {self.col}): {self.val}"
