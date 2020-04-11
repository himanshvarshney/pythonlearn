def person(name,**data):
    print(name)
    for i,j in data.items():

        print(i,"=",j)

person('Himanshu', age = 28, city ="Delhi", mob= 9818472920)