#  Write a program to calculate factorial of a no using while loop
n = int(input("Enter the number:"))
sum = 1
i = 1 
while(i<=n):
    sum *= i
    i += 1 
    
print(f"The factorial of the number is {sum}")