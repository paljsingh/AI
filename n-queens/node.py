from pos import Pos

class Node:

    def __init__(self, pos: Pos):
        self.parent = None
        # we have N child nodes
        self.child = list()
        self.pos = pos

    def __str__(self):
        return "parent: {}, child: {}, pos: {}".format(self.parent, ':'.join(self.child), self.pos)


