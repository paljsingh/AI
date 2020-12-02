
from __future__ import annotations
class Pos:

    def __init__(self, row=-1, col=-1):
        self.row = row
        self.col = col

    def __eq__(self, other: Pos):
        return self.row == other.row and self.col == other.col


    def __str__(self):
        return "row: {}, col: {}".format(self.row, self.col)