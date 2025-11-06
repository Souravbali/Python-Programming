#  Write a program count no of vowels, consonants, digits and
# length of the string. 
string = input().strip()
vowels = 0 
consonants = 0 
digit = 0 

for char in string:
    if char.isdigit():
        digit += 1 
    elif char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1 
        else:
            consonants += 1 

print("Length:", len(string))
print("Digit:", digit)
print("Vowels:", vowels)
print("Consonant:", consonants)