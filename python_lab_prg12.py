name = 'sourav'
name_2 = 'bali'
#length of the string 
print(len(name))
print(len(name_2))
print(len(name))

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