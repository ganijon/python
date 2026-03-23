from copy import deepcopy # import function 'deepcopy' from the module 'copy'

import copy as cp   # import whole 'copy' library as 'cp' 

# import numpy as np  # numpy library is not part of python

a = [1,2,3]
b = cp.deepcopy(a)

print(b)
print(a is b) # False