# prg_1  Write a Program for arithmetic operations like addition, subtraction, multiplication, and remainder.
a = int(input("Enter the first operand:"))
op = input("Enter the operator:")
b = int(input("Enter the second operand:"))

if op == '+':
    print(a+b)

elif op == '-':
    print(a-b)   

elif op == '*':
    print(a*b) 

elif op == '%':
    print(a%b)
 
elif op == '/':
      if b == 0:
          print("infinity")
      else:
          print(a/b)

else:
    print("invalid input")
           
