#!/usr/bin/env python3

from typing import List
from node import Node
import argparse

class Coloring:

    def __init__(self, matrix: List[List[int]], colors: List[str]):
        self.matrix = matrix
        self.colors = colors
        self.node_count = 0
        self.number_of_solution = 0

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

            if len(node.child) == 0 and node.level == len(self.matrix):
                self.number_of_solution += 1
                self.show_path(node)

    def can_assign_to_child(self, node: Node, color: str):
        tmp_node = node
        while tmp_node.level > 0:
            if self.matrix[node.level][tmp_node.level-1] and tmp_node.color == color:
                return False
            tmp_node = tmp_node.parent

        return True

    def solve_by_dfs_backtrack(self, node: Node):
        for color in self.colors:
            next_level = node.level + 1
            if next_level <= len(self.matrix):
                self.node_count += 1
                if self.can_assign_to_child(node, color):
                    child_node = Node(self.node_count, next_level, color)
                    node.child.append(child_node)
                    child_node.parent = node

                    self.solve_by_dfs_backtrack(child_node)

    def get_adjacent_nodes(self, node: Node, nodes: List[Node]):
        adjacent_nodes = list()
        for tmp_node in nodes:
            if tmp_node == node:
                continue

            if self.matrix[node.num][tmp_node.num] == 1:
                adjacent_nodes.append(tmp_node)

        return adjacent_nodes

    def filter_nodes(self, nodes: List[Node], color: str, test=False):
        success = True
        color_options = list()
        for node in nodes:
            if node.color:
                continue

            if len(node.color_options) > 0:
                if test:
                    color_options = node.color_options.copy()
                else:
                    node.color_options.remove(color)
                    color_options = node.color_options

                if color in color_options:
                    color_options.remove(color)

            if not color_options or len(color_options) == 0:
                success = False
        return success

    def reset_colors(self, nodes: List[Node]):
        # assign color options to all the nodes.
        for node in nodes:
            node.set_color_options(self.colors)

    def is_adjacent_color(self, nodes: List[Node], color):
        for node in nodes:
            if node.color == color:
                return True
        return False

    def solve_by_filtering(self):
        nodes = list()

        for k in range(len(self.matrix)):
            node = Node(k, 0)
            nodes.append(node)

        self.reset_colors(nodes)

        # Assign one color for a node and filter.
        for node in nodes:
            for color in node.color_options:
                # update adjacent nodes
                adjacent_nodes = self.get_adjacent_nodes(node, nodes)
                if not self.is_adjacent_color(adjacent_nodes, color) and self.filter_nodes(adjacent_nodes, color, True):
                    node.color = color
                    node.color_options = [color]
                    self.filter_nodes(adjacent_nodes, color, False)
                    break

        for node in nodes:
            print(node)

parser = argparse.ArgumentParser(                                                                               # noqa
    description='Graph coloring problem - python implementation.', formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-m', '--method', choices=['backtrack', 'filtering'], default='backtrack',
                    help='method name. (default=backtrack)')
app_args = parser.parse_args()


if __name__ == '__main__':
    graph_matrix = [
        [0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 1, 0],

    ]
    colors = ['RED', 'GREEN', 'BLUE']
    coloring = Coloring(graph_matrix, colors)
    head = Node(0)

    if app_args.method == 'backtrack':
        coloring.solve_by_dfs_backtrack(head)
        coloring.show_solutions(head)
        print("Total solutions: {}".format(coloring.number_of_solution))
    elif app_args.method == 'filtering':
        coloring.solve_by_filtering()
