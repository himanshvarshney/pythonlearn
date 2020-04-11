f1= open("IMG.JPG","rb")

#print(f1.read())

f2 = open('MyPic.JPG','wb')

for data in f1:
    print(data)
    f2.write(data)