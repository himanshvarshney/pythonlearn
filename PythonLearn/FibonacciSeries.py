def fibo(n):
    if n<=1:
        print(0)
    else:
        a=0
        b=1
        print(a)
        print(b)
        for i in range(2, n):
            c=a+b

            a=b
            b=c

            print(c)

def fibomax(n):
    if n<=1:
        print(0)
    else:
        a=0
        b=1
        print(a)
        print(b)

        for i in range(2,n):
            c=a+b
            if c<n:
                a=b
                b=c
                print (c)
            else:
                break
fibo(10)

fibomax(1452)