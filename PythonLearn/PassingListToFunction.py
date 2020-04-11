


def passingList(lst):
    even=0
    odd=0

    for i in lst:
        if i%2 ==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst = [51,24,25,98,1,254,25]

print(lst)
even,odd =passingList(lst)

print("even numbers are : {} and odd numbers are : {}".format(even,odd))