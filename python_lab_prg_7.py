# Write a program to check whether the given no is Armstrong or not using while loop.
num = input("Enter the number")
total = 0 
i = 0 

while i < len(num):
    total = total + int(num[i]) ** 3
    i = i+1 

if num == total:
    print(f"the {num} is armstrong number")

else:
    print(f"{num} is not armstrong number")
