from array import *

arr = array('i',[])

n = int(input('Enter the size of array'))

for i in range(n):
    x = int(input('Enter the next value'))
    arr.append(x)

print(arr)

val = int(input('Enter the value to be search'))
k=0
for e in arr:
    if e==val:
        print(e)
        break
    k+=1