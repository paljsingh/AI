from __future__ import annotations
from typing import List


class Node:

    def __init__(self, num: int, level: int=0, color=None):
        self.num = num
        self.level = level
        self.color = color
        self.child = list()
        self.parent = None

        self.color_options = set()

    def set_color_options(self, colors: List):
        self.color_options = set().union(colors)

    def __str__(self):
        return "Node: {}, Color: {}".format(self.num, self.color)

    def __eq__(self, other: Node):
        return self.num == other.num

    def __hash__(self):
        hash(self.num)