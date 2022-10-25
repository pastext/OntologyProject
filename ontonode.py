from __future__ import annotations

class WrongDirectionError(Exception):
    pass

ontology = {
    'classes': {},
    'relations': {},
    'class_elements': {},
    'relations_elements': {}
}

class Node:
    def __init__(self, left = None, right = None, type = 'class', name = 'a'):
        self.left = left
        self.right = right
        self.type = type
        self.name = name
        
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

    def __str__(self) -> str:
        return f'Наименование: {self.name}, Тип: {self.type} \n Левый потомок: {self.left} / Правый потомок {self.right}'
