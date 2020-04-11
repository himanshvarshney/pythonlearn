a=15
b=20
print(a,b)
def variableCheck():
    globals()['a']=10
    a=20
    b=21
    print(a,b)


variableCheck()
print(a,b)