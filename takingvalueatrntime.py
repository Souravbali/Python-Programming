tup_num = int(input())
tup = []
for i in range(tup_num):
    value = int(input(f"enter the element{i+1}"))
    tup.append(value)
tup_value = tuple(tup)
print("The entered tuple element is:",tup_value)