pos = -1

def search(list,n):
    i=0
    for i in list:
        if(i==n):
            globals()['pos'] = i.__index__()
            return True
    else:
        return False

list = [25,65,14,98,56,39,47,51]
n = int(input('Enter the number to be searched'))


if search(list,n):
    print("Found at",pos)
else:
    print("Not Found")