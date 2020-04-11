

pos = -1


def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False

list = [25,54,98,652,145,78,54]
n = int(input("Enter the number to be searched from List"))

if search(list,n):
    print("Found at",pos)
else:
    print("No Found")