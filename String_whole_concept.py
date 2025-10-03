#concept of slicing of the string  
'''
Write a program string is a palidrome or not 
'''
string = input("Enter the string:")
string2 = string[::-1]

if string.lower() == string2.lower():
    print("Number is palidrome")
else:
    print("Number is not palidrome")

#concetination of string 
name = "Sourav"
last_name = "Bali"
print(name+last_name)
 
name_2 = "Reemu"
last_name = "Bali"
print(name_2+last_name)

#length of the string 
print(len(name))
print(len(name_2))
print(len(name))

#slicing from the positive index 
name = "My name is Sourav bali I am i Bca sem 111"
temp_store = name[0:15:2]
print(temp_store)

name = "bealkwarldoolol"
store = name[0:15:2]
print(store)

# loweercase all the string
names = "ALICE IN BORDER LAND"
print(names.lower())
# uppercase all the string 
namess = "alice in border land"
print(namess.upper())
#captalized method capital only first letter of the strig sentence
name = "alice in border land"
print(name.capitalize())

# repace method means replace string sentences
name = "I am sourav bali , i am from jammu , i live in my home , i am sourav"
print(name.replace("sourav","Gourav",2))
# jitne tum number utne changes krega like maine 2 likha 

#strip() method
name = "    souravbali"
print(name.strip())
# rstrip() method 
name = "     sourav     "
print(name.strip())

#split() method 
name = "23 05 20 11"
n = name.split()
print(n)
