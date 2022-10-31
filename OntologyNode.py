from __future__ import annotations

class SomethingWrong(Exception):
    pass

ontology = {
    'classes': {},
    'relations': {},
    'class_elements': {},
    'relations_elements': {}
}

class Node:
    def __init__(self, left = None, right = None):#, type = 'class', name = 'a'):
        self.left = left
        self.right = right
        #self.type = type
        #self.name = name
        
    def menu(self):
        x = -1
        while x != 0:
            print("For adding class press [1]")
            x = int(input())
            if x == 1:
                #self = self.add_class()
                self.right.add_to_list()
            elif x == 2:
                self.right.outputting_list()
                self.outputting_tree()

    def outputting_tree(self):
        print(self.right.right)
        if self.left is not None:
            self.left.outputting_tree()

    def outputting_list(self):
        print(self.right)
        if self.left is not None:
            self.left.outputting_list()
    
    def add_to_list(self):
        name = input('Name of class\n')
        if self.left:
            self.adding(self.left, name)
        else:
            self.left = Node(right = name)

    def adding(self, next: Node, name):
        that = self
        while (next.left is not None) and (next.right < name):
            that = next
            next = next.left
        if next.right == name:
            print('Already exist\n')
        elif next.right > name:
            that.left = Node(left = next, right = name)
        else:
            next.left = Node(right = name)
    
    def delete_from_list(self):
        if self.left:
            name = input('Name of class\n')
            that = self
            next = self.left
            while (next.left is not None) and (next.right < name):
                that = next
                next = next.left
            if next.right == name:#Нужно ещё удалять из классов, отношений, эл. кл., эл. от.
                that.left = next.left
                next = None
            else:
                print('Нет такого')
        else:
            print('Удалять нечего')

               
class Root(Node):
        def __init__(self):
            self.__make_ontotree__()
            self.c = self.right
            self.r = self.left.right
            self.ce = self.left.left.right
            self.re = self.left.left.left.right

        def pr(self):
            print(self.c.right, self.r.right, self.ce.right, self.re.right)    
        
        def __make_ontotree__(self):
            self.right = Node(right = 'Classes')
            self.left = Node(right = Node(right = 'Relations'))
            self.left.left = Node(right = Node(right = 'Class elements'))        
            self.left.left.left = Node(right = Node(right = 'Relations elements'))

        def menu(self):
            x = -1
            while x != 0:
                x = int(input("Press:\n[1]For adding something\n[2]For see tree\n[3]For delete something\n"))
                if x == 1:
                    x = int(input(" Press:\n [1]For add class\n [2]For add relation\n"))
                    if x == 1:
                        self.c.add_to_list()
                    elif x == 2:
                        self.r.add_to_list()
                elif x == 2:
                    self.c.outputting_list()
                    self.r.outputting_list()
                    self.outputting_tree()
                elif x == 3:
                    x = int(input(" Press:\n [1]For delete class\n [2]For delete relation\n"))
                    if x == 1:
                        self.c.delete_from_list()
                    elif x == 2:
                        self.r.delete_from_list()



tree = Root()
tree.pr()
tree.menu()
#print(None == "aaaa")