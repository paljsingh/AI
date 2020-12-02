#!/usr/bin/env python3

from typing import List
from node import Node

class Coloring:

    def __init__(self, matrix: List[List[int]], colors: List[str]):
        self.matrix = matrix
        self.colors = colors
        self.node_count = 0
        self.number_of_solution = 0

    def get_next_color(self, color: int):
        return self.colors[(color + 1) % len(self.colors)]

    def show_path(self, node: Node):
        tmp_node = node
        stack = list()
        while tmp_node.level > 0:
            stack.append(tmp_node)
            tmp_node = tmp_node.parent

        count = 0
        while len(stack) > 0:
            tmp_node = stack.pop()
            count += 1
            print("Node: {}, Color: {}".format(count, tmp_node.color))

        print("-------\n")

    def show_solutions(self, head: Node):
        """
        traverse as BFS, every time a leaf node is found, show the path from root to lead node.
        :param head:
        :return:
        """
        expanded_queue = list()
        expanded_queue.append(head)

        while len(expanded_queue) > 0:
            node = expanded_queue.pop(0)
            for child_node in node.child:
                expanded_queue.append(child_node)

            if len(node.child) == 0:
                self.number_of_solution += 1
                self.show_path(node)

    def can_assign_to_child(self, node: Node, color: str):
        tmp_node = node
        while tmp_node.level > 0:
            if self.matrix[node.level][tmp_node.level-1] and tmp_node.color == color:
                return False
            tmp_node = tmp_node.parent

        return True

    def m_coloring(self, node: Node):
        for color in self.colors:
            next_level = node.level + 1
            if next_level <= len(self.matrix):
                self.node_count += 1
                if self.can_assign_to_child(node, color):
                    child_node = Node(self.node_count, next_level, color)
                    node.child.append(child_node)
                    child_node.parent = node

                    self.m_coloring(child_node)

if __name__ == '__main__':
    matrix = [
        [0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 1, 0],

    ]
    colors = ['R', 'G','B']
    coloring = Coloring(matrix, colors)
    head = Node(0)

    # coloring.show(head)
    coloring.m_coloring(head)
    coloring.show_solutions(head)
    print("Total solutions: {}".format(coloring.number_of_solution))
