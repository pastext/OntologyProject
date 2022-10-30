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
                self.add_class_1()
            elif x == 2:
                self.outputting_right()
    
    def outputting_right(self):
        print(self.right)
        if self.left is not None:
            self.left.outputting_right()
    
    def add_class_1(self):
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

    def add_class(self):
        if self is not None:
            name = input('Name of class\n')
            if self.right == None:
                self.right = name
            else:
                if self.left is not None:
                    if self.left.right == None:
                        self.left.right = name
                    else:
                        self.add(name)
                else:
                    self.left = Node(right = name)

        else:
            raise SomethingWrong

    def add(self, name):
        left = self.left
        if (left.left is not None) and (left.right < name):
            self.left.add(name)
        elif left.right == name:
            print('Already exist\n')
        elif left.right > name:
            self.left = Node(left = left, right = name)
        else:
            left.left = Node(right = name)


    def add_class1(self):
        if self is not None:
            name = input('Name of class\n')
            if self.right == None:
                self.right = name
            else:
                self = self.add(name)
        else:
            raise SomethingWrong

    def add2(self, name):
        if (self.left is not None) and (self.right < name):
            self.left.add(name)
        elif self.right == name:
            print('Already exist\n')
        elif self.right > name:
            print(self.right)
            self = Node(left = self, right = name)
            print(self.right, self.left.right)
        else:
            self.left = Node(right = name)
               

tree = Node(left = Node(right = 'dac'), right = 'bac')
#tree = Node()
tree.menu()