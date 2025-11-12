tup =('s','o','u','o','o')
print(tup.count('o'))

# tuple slicing 
tup = (1,3,4,5,5)
tup2 = tup[1:3]
print(tup2)
'''
Note:- we can access tuple element but cannot change its itz element bcs tuple is immutable

'''
# length and count of the tuple
fruit = eval(input())
print(fruit.count("Mango"))
print(len(fruit))
# reverse the tuple 
fruit = tuple("MANGO")
f = fruit[::-1]
print(f)

# taking user input from mapping 
fruit = tuple(map(str,input().split()))
f = fruit[::-1]
print(f)

