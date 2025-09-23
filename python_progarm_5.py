# Write a program to input a no from the user and generate table of the no using for loop
n = int(input("Enter the table:"))
for i in range(1,11):
    print(f"{n}x{i}={n*i}")
