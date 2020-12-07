
level = 0
def indent():
    global level
    level += 1

def unindent():
    global level
    level -= 1



class BehaviorTree:
    FAIL, RUNNING, SUCCESS = -1, 0, 1

    def __init__(self, root_node):
        self.root = root_node

    def run(self):
        self.root.run()



    @staticmethod
    def build(dict):
        return BehaviorTree(build_node(dict))

class Node:
    def add_child(self, child):
        self.children.append(child)
    def add_children(self, *children):
        for child in children:
            self.children.append(child)


class SelectorNode(Node):
    def __init__(self, name):
        self.children = []
        self.name = name
        self.prev_running_pos = 0

    def run(self):
        for pos in range(self.prev_running_pos, len(self.children)):
            result = self.children[pos].run()
            if BehaviorTree.RUNNING == result:
                self.prev_running_pos = pos
                return BehaviorTree.RUNNING
            elif BehaviorTree.SUCCESS == result:
                self.prev_running_pos = 0
                return BehaviorTree.SUCCESS
        self.prev_running_pos = 0
        return BehaviorTree.FAIL



class SequenceNode(Node):
    def __init__(self, name):
        self.children = []
        self.name = name
        self.prev_running_pos = 0

    def run(self):
        for pos in range(self.prev_running_pos, len(self.children)):
            result = self.children[pos].run()
            if BehaviorTree.RUNNING == result:
                self.prev_running_pos = pos
                return BehaviorTree.RUNNING
            elif BehaviorTree.FAIL == result:
                self.prev_running_pos = 0
                return BehaviorTree.FAIL
        self.prev_running_pos = 0
        return BehaviorTree.SUCCESS



class LeafNode(Node):
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def add_child(self, child):
        pass

    def add_children(self, *children):
        pass

    def run(self):
        return self.func()

def build_node(dict):
    name = dict["name"]
    clazz = dict["class"]
    if clazz == LeafNode:
        func = dict["function"]
        return clazz(name, func)

    node = clazz(name)
    children = dict["children"]
    for child in children:
        node.add_child(build_node(child))

    return node
