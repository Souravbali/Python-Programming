tup1 = (1,3,4,5,6,7)
print(tup1)
print(type(tup1))

# taking user input in tuple 
tup1 = eval(input())
print(tup1)
print(type(tup1))

# taking user input from mapping
tup1 = tuple(map(int, input("Enter numbers: ").split()))
print(tup1)
print(type(tup1))

# taking user input from in different line
n = int(input("Enter the number of elements: "))
a = []
for i in range(n):
    val = input(f"Enter element {i+1}: ")
    a.append(val)
t = tuple(a)
print(t)

# another way 
a = input("Enter elements separated by spaces: ").split()
t = tuple(a)
print(t)
