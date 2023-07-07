import json
from typing import Any
from OntologyNode import Root

tree = Root()
#tree.menu()

# def coder(self):
    # if self.left == None:
    #     LeftNone = True
    # if self.right == None:
    #     RightNone = True
    # if LeftNone 
#     try:
#         if self.right != None:
#             json.dumps()
#     except:
#         pass


# def jsonsaver(self):

# print(json.dumps(tree, default=lambda x:__dict__))

class TestEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        return {'right': o.right, 'left': o.left}
    
print(json.dumps(tree, indent=3, cls=TestEncoder))