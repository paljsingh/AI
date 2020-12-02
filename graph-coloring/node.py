
class Node:

    def __init__(self, num: int, level: int=0, color=None):
        self.num = num
        self.level = level
        self.color = color
        self.child = list()
        self.parent = None

    def __str__(self):
        return "[name: {}, level: {}, color: {}, parent: {}, childern: {}]".format(
            self.num, self.level, self.color, self.parent.num if self.parent else "None", ' '.join([str(x.num) for x in self.child]) )

