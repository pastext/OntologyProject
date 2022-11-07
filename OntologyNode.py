from __future__ import annotations
from unicodedata import name
#from unicodedata import name

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

    #Нормальное добавление в ветку, которая является
    # правым потомком узла, в котором вызван метод ↵
    #   ⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓
    def add_to_list(self, object: str = 'object'):
        name = input(f'Name of adding  {object}\n')
        if self.right != None:
            curr = self.right
            while (curr.left != None) and (curr.right < name):
                curr = curr.left
            if curr.right == name:
                print('Already exist\n')
            elif curr.right > name:
                curr.left = Node(left = curr.left, right = curr.right)
                curr.right = name
            else:
                curr.left = Node(right = name)
        else:
            self.right = Node(right = name)

    def add_to_list_unnamed(self, name):#, object: str = 'object'):
        if self.right != None:
            curr = self.right
            while (curr.left != None) and (curr.right < name):
                curr = curr.left
            if curr.right == name:
                print('Already exist\n')
            elif curr.right > name:
                curr.left = Node(left = curr.left, right = curr.right)
                curr.right = name
            else:
                curr.left = Node(right = name)
        else:
            self.right = Node(right = name)
    #   ⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑
    
    #Нормальное удаление в ветке, которая является
    # правым потомком узла, в котором вызван метод ↵
    #   ⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓    
    def delete_from_list(self, object: str = 'object'):
        if self.right != None:
            name = input(f'Name of deleting {object}\n')
            prev = self
            curr = self.right
            while (curr.left is not None) and (curr.right < name):
                prev = curr
                curr = curr.left
            if curr.right == name:#Нужно ещё удалять из классов, отношений, эл. кл., эл. от.
                if self != prev:
                    prev.left = curr.left
                else:
                    prev.right = curr.left
                curr = None
            else:
                print('Нет такого')
        else:
            print('Удалять нечего')
    #   ⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑⇑
   
    def add_to_list_(self, object: str = 'object'):
        name = input(f'Name of adding {object}\n')
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

    def delete_from_list_(self, object: str = 'object'):
        if self.left:
            name = input(f'Name of deleting {object}\n')
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

    def add_element_to_class(self):#Только начал
        name = input('Name of class\n')
        if self.left:
            pass
        else:
            self.left = Node(right = Node(left = name, right = f'Elements of {name}'))
            name = input('Name of element\n')



               
class Root(Node):
    def __init__(self):
        self.__make_ontotree__()
        self.elements = self
        self.classes = self.left
        self.relations = self.left.left
        self.classes_elements = self.left.left.left
        self.relations_elements = self.left.left.left.left
        #self.__menu__()

    def pr(self):
        print(self.elements.right, self.classes.right, 
        self.relations.right, self.classes_elements.right, 
        self.relations_elements.right)    
        
    def __make_ontotree__(self):
        self.right = None
        self.left = Node(
            left = Node(
                left = Node(
                    left = Node()                        
        )))

    def __make_ontotree_test__(self):
            self.right = Node(right = 'Elements')
            self.left = Node(right = Node(right = 'Classes'))
            self.left.left = Node(right = Node(right = 'Relations'))        
            self.left.left.left = Node(right = Node(right = 'Classes\' elements'))
            self.left.left.left.left = Node(right = Node(right = 'Relations\' elements'))

    def menu(self):
            x = -1
            while x != 0:
                x = int(input("Press:\n[1]For adding something\n[2]For see tree\n" 
                "[3]For delete something\n"))
                if x == 1:
                    x = int(input(" Press:\n [1]For add element\n [2]For add class\n"
                    " [3]For add relation\n"))
                    if x == 1:
                        self.elements.add_to_list('element')
                    elif x == 2:
                        self.classes.add_to_list('class')
                    elif x == 3:
                        self.relations.add_to_list('relation')
                elif x == 2:
                    self.elements.right.outputting_list() if self.elements.right != None\
                         else print('Empty')
                    self.classes.right.outputting_list() if self.classes.right != None\
                         else print('Empty')
                    self.relations.right.outputting_list() if self.relations.right != None\
                         else print('Empty')
                    #self.outputting_tree()
                elif x == 3:
                    x = int(input(" Press:\n [1]For delete element\n [2]For delete class\n"
                    " [3]For delete relation\n"))
                    if x == 1:
                        self.elements.delete_from_list('element')
                    elif x == 2:
                        self.classes.delete_from_list('class')
                    elif x == 3:
                        self.relations.delete_from_list('relation')

    def add_element(self):
        name
        self.elements.add_to_list('element')
        

    def add_element_to_class(self):#Только начал
        name = input('Name of class\n')
        if self.classes_elements.right != None:
            pass
        else:
            self.classes_elements.right = Node(right = Node(left = name))
            #self.classes.add_to_list()
            name = input('Name of element\n')
            self.classes_elements.right.right.add_to_list('element')#тут будет функция с вводом названия элемента
            #self.elements.add_to_list()



tree = Root()
#tree.pr()
tree.menu()