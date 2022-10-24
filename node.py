class Node:
    def __init__(self) -> None:
        self.left = None
        self.right = None

def make_tree(tree: Node):
    tree.left: Node
    tree.left.left = Node
    x = 1
    tree.right = x
    x = x + 1
    tree.left.right = x
    x = x + 1
    tree.left.left.right = x

def output(tree: Node):
    print(tree.right)
    print(tree.left.right)
    print(tree.left.left.right)

t = None
make_tree(t)
output(t)
