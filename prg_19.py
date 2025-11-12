my_list = [1, 2, 3, 2, 4, 2, 5]
count_two = my_list.count(2)
print("Count of 2:", count_two)
index_four = my_list.index(4)
print("Index of 4:", index_four)
new_elements = [6, 7, 8]
my_list.extend(new_elements)
print("After extend:", my_list)
popped_element = my_list.pop()
print("Popped element:", popped_element)
print("After pop:", my_list)
my_list.clear()
print("After clear:", my_list)