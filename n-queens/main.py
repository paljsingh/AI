from typing import Dict
from node import Node
from pos import Pos
import sys

class NQueens:

    def __init__(self, size: int):
        self.size = size
        self.solution_count = 0
        self.board = list()

        for i in range(self.size):
            row = list()
            for j in range(self.size):
                row.append(0)

            self.board.append(row)

    def show_board(self, queens_pos: Dict[int, Pos] =None):
        if queens_pos is None:
            queens_pos = dict()

        whitebg = "\033[47m"
        resetbg = "\033[0m"
        blackbg = "\033[40m"
        textcolor = "\033[1;31m"
        for i in range(self.size):
            for j in range(self.size):
                if Pos(i, j) in queens_pos.values():
                    if (i + j) % 2:
                        print(textcolor + whitebg + " ♛ " + resetbg, end="")
                    else:
                        print(textcolor + blackbg + " ♛ " + resetbg, end="")

                else:
                    if (i + j) %2:
                        print(textcolor + whitebg + "   " + resetbg, end="")
                    else:
                        print(textcolor + blackbg + "   " + resetbg, end="")
            print("")
        print("----------------")

    def is_queen_at_diagonal(self, pos: Pos, queens_pos: Dict[int, Pos]):
        # assume, pos has a queen on it.
        up_right = [-1, +1]
        down_right = [+1, +1]
        up_left = [-1, -1]
        down_left = [+1, -1]

        directions = [up_right, down_right, up_left, down_left]

        for (i, j,) in directions:
            next_row = pos.row + i
            next_col = pos.col + j
            while True:
                if next_row < 0 or next_row >= self.size or next_col < 0 or next_col >= self.size:
                    break

                if Pos(next_row, next_col) in queens_pos.values():
                    return True

                next_row = next_row + i
                next_col = next_col + j

        return False

    def is_queen_at_column(self, pos: Pos, queens_pos: Dict[int, Pos]):
        for row in range(self.size):
            if row == pos.row:
                continue
            if Pos(row, pos.col) in queens_pos.values():
                return True
        return False


    def is_available(self, pos: Pos, queens_pos: Dict[int, Pos]):
        return not self.is_queen_at_diagonal(pos, queens_pos) and not self.is_queen_at_column(pos, queens_pos)

    def solve(self, node: Node, row: int, queens_pos_orig: Dict[int, Pos]):

        if row < 0 or row >= self.size:
            return

        queens_pos = queens_pos_orig.copy()

        for col in range(self.size):
            if self.is_available(Pos(row, col), queens_pos):
                queens_pos[row] = (Pos(row, col))
                child_node = Node(Pos(row, col))
                child_node.parent = node
                node.child.append(child_node)

                if row == self.size - 1:
                    self.show_board(queens_pos)
                    self.solution_count += 1

                self.solve(node, row+1, queens_pos)

                # restore from original copy, discard any elements added by recursive calls.
                queens_pos = queens_pos_orig.copy()


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("usage: python3 ./main.py N")
        print("N is any number <=1 N <= 16 (ideally)")
        exit(1)

    board = NQueens(int(sys.argv[1]))
    head = Node(Pos())
    queens_pos = dict()

    board.solve(head, 0, queens_pos)
    print("Total Solutions: {}".format(board.solution_count))
