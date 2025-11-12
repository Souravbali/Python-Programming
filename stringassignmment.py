string = "soubali987bali"
print(string.isalnum())

# minimum character in the string 
string = "mynameissourav"
print(min(string))

#  maximum character in the string 
string = "souravvv"
print(max(string))

#  convert the string into the length 
string = "sourav"
print(list(string))

# remove the specific character 
string = "Banana"
print(string.replace("a",'e'))  # very  important concept

# count of the occurance 
string = "My name is sourav bali and my is name is is sourav bali "
print(string.count("is"))

# print ascii values 
string = "sourav"
for i in string:
    print(ord(i),end=" ")

