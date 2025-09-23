base = int(input("Enter the base:"))
power = int(input("Enter the power:"))
total = 1
while power>0:
    total *= base
    power -= 1

print(f"the result is {total}")