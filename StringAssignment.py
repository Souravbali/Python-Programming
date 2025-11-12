# reverse the string 
string = "My name is sourav bali"
print(string[::-1])

#  string ko list bnana fir use fir se list bnana 
string = input().split()
print(string)
print(",".join(string))
# 10. Find a Substring 
# Problem: Find the index of "World" in "Hello World". 
# Solution: 
# python 
# Copy code 
# str1 = "Hello World" 
# index = str1.find("World") 
# print(index)  # Output: 6 
string1 = "hello world "
index = string1.find("world")
print(index)

string = "My name is Sourav bali "
index = string.find("a",10 ,20)  # find a from index 10 to 20
print(index)