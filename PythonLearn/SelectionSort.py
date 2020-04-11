def sort(list):

    for i in range(7):
        minpos = i
        for j in range(i,8):
            if list[j] < list[minpos]:
                minpos = j


        temp = list[i]
        list[i] = list[minpos]
        list[minpos]= temp






list = [2,5,9,7,4,6,8,1]
sort(list)
print(list)