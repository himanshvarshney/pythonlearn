def bubbleSort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if(list[j]>list[j+1]):
                temp = list[j]
                list[j]=list[j+1]
                list[j+1]=temp


list = [25,65,75,41,98,47]
bubbleSort(list)
print(list)