a=5
b=2
try:
    print(a/b)
    input = int(input("Enter any number"))
    print(input)
except ZeroDivisionError as e:
    print("Divide by zero",e)
except ValueError as e:
    print("Illegal value entered")
except Exception as e:
    print("Something went wrong")

finally:
    print("Closing files")

print("great")