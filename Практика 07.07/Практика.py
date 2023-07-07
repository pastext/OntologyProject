import json

def menu(classes):
    # try:
        k = int(input('1 - create class, 2 - fill class, 3 - create relation, 4 - fill relation, 5 - print '))
        if k == 1:
            create_class(classes)
        elif k == 2:
            fill_class(classes)
        elif k == 3:
            create_relation(relation)
        elif k == 4:
            fill_relation(relation)
        elif k == 5:
            print(classes)
            print(relation)
        elif k == 6:
            with open('classes.json', 'w') as clfile:
                json.dump(classes, clfile)
        elif k == 7:
            with open('classes.json', 'r') as clfile:
                classes = json.load(clfile)
        menu(classes)
    # except:
    #     print('exeption')
    #     menu()

def create_class(classes):
    classes.setdefault(input('class name '), [])

def fill_class(classes):
    #classes.setdefault(input('class name '), {}).setdefault(input('element '), {})
    classes.setdefault(input('class name '), []).append(input('element '))

def create_relation(relation):
    relation.setdefault(input('relation name '), {})

def fill_relation(relation):
    relation.setdefault(input('relation name '), {}).setdefault(input('first '), set()).add(input('second '))

classes = {}
relation = {}

menu(classes)