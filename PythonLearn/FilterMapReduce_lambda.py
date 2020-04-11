from functools import reduce


nums = [3,5,9,5,4,12,5,154,255,236,9]

even = list(filter(lambda n:n%2==0,nums))
odds = list(filter(lambda n:n%2==1,nums))
doubles = list(map(lambda n:n*2,even))
add_all = reduce(lambda a,b:a+b,doubles)


print("odds numbers are : {} and evens number are: {}".format(odds,even))
print(doubles)
print(add_all)