def count_vowel(input_string):
    vowel = 'aeiouAEIOU'
    count = 0 
    for char in input_string:
        if  char in vowel:
            count += 1 
    return count

user_string = input("Enter the string")
counting = count_vowel(user_string)
print(f"count of the vowel is :{counting}")

