tuple1 = tuple(map(int,input().split()))
tuple2 = tuple(map(int,input().split()))

concat_tuple = tuple1 + tuple2

repeated_tuple = tuple1 * 3

element_to_check = 2
is_member = element_to_check in tuple1

# Print the results
print("Concatenation of tuples:", concat_tuple)
print("Repetition of tuple1 three times:", repeated_tuple)
print(f"Is {element_to_check} in tuple1?:", is_member)
