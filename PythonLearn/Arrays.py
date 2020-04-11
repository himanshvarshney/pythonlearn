from array import *

vals = array('i',[5,8,6,9,1])

print(vals.buffer_info()) # buffer_info() give address and size of array

newArr = array(vals.typecode,(a*a for a in vals))

for e in newArr:
    print(e)