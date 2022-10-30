from __future__ import annotations
from re import T

class WrongDirectionError(Exception):
    pass

ontology = {
    'classes': {},
    'relations': {},
    'class_elements': {},
    'relations_elements': {}
}

class Node:
    def __init__(self, left=None, right=None):#, type = 'class', name = 'a'):
        self.left = left
        self.right = right
        #self.type = type
        #self.name = name
        
    def make_child(self, child, direction: str ='left'):
        if direction == 'left':
            self.left = child
        elif direction == 'right':
            self.right = child
        else:
            raise WrongDirectionError
    
    def get_child(self, direction: str='left') -> Node:
        if direction == 'left':
            return self.left
        elif direction == 'right':
            return self.right
        else:
            raise WrongDirectionError

    def menu(self):
        x = -1
        while x != 0:
            print("For adding class press [1]")
            x = int(input())
            if x == 1:
                #self = self.add_class()
                self.add_class()
            elif x == 2:
                #while self != None:
                #self.__str__()
                print(self)
                print(self.left)
                print(self.right)
                print(self.left.left)
                print(self.left.right)
        


    def __str__(self) -> str:
        return f'{self.left} / {self.right}'
        
    def add_class1(self):# -> Node:
        #t0 = Node(left = self.left, right = self.right)
        #t = t0.right
        t = self
        name = input('Name of class\n')
        if t != None:
            while (t.left != None) and (t.right < name):        
                #t0 = t
                t = t.left
                #t = t.get_child()
                #t.get_child()
                #t = Node(left = t.left, right = t.right)
        t = Node(left = t, right = name)
        #return t0
        #return self

    def add1(self, name):
        if (self.left != None) and (self.right < name):
            self.left.add(name)
        else:
            self = Node(left = self, right = name)

    def add_class(self):
        name = input('Name of class\n')
        if self != None:
            self = add(self, name)
        
def add(t: Node, name) -> Node:
    if (t.left != None) and (t.right < name):
        t.left = add(t.left, name)
    else:
        t = Node(left = t, right = name)
    return t

tree=Node()

'''ontology['classes']=tree.right
tree.left=Node()
ontology['relations']=tree.left.right
tree.left.left=Node()
ontology['class_elements']=tree.left.left.right
tree.left.left.left=Node()
ontology['class_elements']=tree.left.left.left.right
'''

def add_class_1(tree: Node):
    #t.right = Node()
    #t.right.right = input('Название класса')
    
    #t0 = tree
    #t = tree
    t = tree#.right
    name = input('Name of class')
    if t == None:
        t = Node(right = name)
    else:
        while (t.left != None) and (t.right < name):        
            #t0 = t
            #t = t.left
            t = t.get_child()
        t = Node(left = t, right = name)






tree.menu()
