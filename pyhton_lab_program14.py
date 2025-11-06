string = input("Enter the string:").strip()
string2 =string[::-1]
if string.lower() == string2.lower():
    print("String is palidrome")
else:
    print("String is not palidrome")