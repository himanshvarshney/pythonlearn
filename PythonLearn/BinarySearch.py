pos = -1

def bubbleSort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if(list[j]>list[j+1]):
                temp = list[j]
                list[j]=list[j+1]
                list[j+1]=temp



def search(list,n):

    l=2
    u=len(list)-1
    while l<=u:
        mid =(l+u)//2

        if(list[mid] == n):
            globals()['pos']=mid
            return True
        else:
            if(list[mid]<n):
                u=mid+1
            else:
                l=mid-1
    return False


list= [52,65,87,41,26,93,2,48,52,12,36,54,84]
bubbleSort(list)
print(list)
n=int(input("Enter the number to be searched"))

if search(list,n):
    print("Found at",pos)
else:
    print("Not Found")