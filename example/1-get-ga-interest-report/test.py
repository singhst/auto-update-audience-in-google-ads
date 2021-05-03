import os
print(">",os.path.abspath(os.path.join('given_path', os.pardir)))


import os
current_dir =  os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(current_dir + "/../../")
print(parent_dir)