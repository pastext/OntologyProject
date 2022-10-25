from ontonode import Node

root = Node(name='Start')

def init_graph(tree_root: Node):
    x = -1
    t: Node = tree_root

    while x != 0:
        child_direction = input('Enter child direction \n')
        child_name = input('Enter class name \n')

        child = Node(name=child_name)
        t.make_child(child, direction=child_direction)

        answer = input('Would you like to add another direction child to current node? y/n \n')
        if answer != 'y':
            t = child
        x = int(input('Whould you like to continue? 1 / 0 \n'))

def dfs(node: Node):
    if node is not None:
        print(node.name)
        dfs(node.left)
        dfs(node.right)


init_graph(root)
dfs(root)

# def menu(self):
#     x = -1
#     while x != 0:
#         print("For adding class press [1]")
#         x = int(input())
#         if x == 1:
#             add_class(self)
#         elif x == -2:
#             #while self != None:
#             self.__str__()


# def add_class(tree: Node):
#     #t.right = Node()
#     #t.right.right = input('Название класса')
    
#     #t0 = tree
#     #t = tree
#     t = tree.right
#     name = input('Name of class')
#     if t == None:
#         t = Node(right = name)
#     else:
#         while (t.left != None) and (t.right < name):        
#             #t0 = t
#             #t = t.left
#             t = t.get_child()
#         t = Node(left = t, right = name)
