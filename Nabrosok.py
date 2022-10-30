from __future__ import annotations

class WrongDirectionError(Exception):
    pass

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
                self.outputting_right()
    
    def outputting_right(self):
        print(self.right)
        if self.left is not None:
            self.left.outputting_right()

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
            print(self.right, left.right)
            self.left = Node(left = left, right = name)
            print(self.right, self.left.right)
            #self.left = left
        else:
            left.left = Node(right = name)


    def add_class1(self):
        if self is not None:
            name = input('Name of class\n')
            if self.right == None:
                self.right = name
            else:
                self = self.add(name)
            return self
        else:
            raise SomethingWrong

    def add2(self, name):
        if (self.left is not None) and (self.right < name):
            self.left.add(name)
            return self
        elif self.right == name:
            print('Already exist\n')
            return self
        elif self.right > name:
            print(self.right)
            self = Node(left = self, right = name)
            print(self.right, self.left.right)
            return self
        else:
            self.left = Node(right = name)
            return self            

    def add1(self, name):
        t = self
        while (t is not None) and (t.right < name):
            t = t.left
        t = Node(left = t, right = name)
               

tree = Node(left = Node(right = 'dac'), right = 'bac')
#tree = Node()
tree.menu()