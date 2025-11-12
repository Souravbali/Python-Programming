def even_odd(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"
    

n = int(input("Enter the number:"))
res = even_odd(n)
print(f"{n} is {res}")