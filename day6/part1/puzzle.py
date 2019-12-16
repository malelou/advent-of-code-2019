class Node:
    def __init__(self, name, children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def add_child(self, node):
        # assert isinstance(node, Node)
        self.children.append(node)

def parse(lines):
    ans = []
    for line in lines:
        if line:
            ans.append([x for x in line.strip().split(")")])
    return ans

def solve(data):
    nodes = []
    for item in data:
        if(next((n for n in nodes if n.name == item[0]), None) == None):
            nodes.append(Node(item[0]))
    
    for item in data:
        parentNode = next((n for n in nodes if n.name == item[0]), None)
        parentNode.add_child(next((n for n in nodes if n.name == item[1]), None))
    return nodes

