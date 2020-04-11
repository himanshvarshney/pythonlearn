import sys

print(sys.getrecursionlimit())

def greet():
    print("Hey Hi Good Morning")
    greet()
greet()