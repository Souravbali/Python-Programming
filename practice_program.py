# write a program to accept name from the user and display the name with welcome message on screen
name = input("Enter the name:")
print(name)

# question 2 Write a program to accept 3 number from user calculate sum and average 
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))
sum = number_1+number_2+number_3
print(sum)
average = (number_1+number_2+number_3)/3
print(average)

# qno.3 Write a program to store string literal and format the string
name = "Sourav bali"
age = 24
paragraph = "My name is {}\nI am from jammu \nI Love to study books and Novels \nMy age is {}".format(name,age)
print(paragraph)

#  qno.4 Write a program to accept marks of 5 students from user calculate total , 
# calculate the percentage , print result fail or pass
science_marks = int(input("Enter the marks  of first subject:"))
politics_marks = int(input("Enter the marks  of second subject:"))
English_marks = int(input("Enter the marks  of third subject:"))
Hindi_marks = int(input("Enter the marks  of fourth subject:"))
Math_marks = int(input("Enter the marks  of  fifth subject:"))
total_marks = 500
mark_obtain = (science_marks + politics_marks +English_marks +Hindi_marks+Math_marks)
print(mark_obtain)
percentage = mark_obtain/total_marks*100
print(percentage)
if(percentage>=95):
    print("A")
elif (percentage>=85 and percentage<95):
    print("B")
elif (percentage>=75 and percentage<85):
    print("c") 
elif (percentage>=60 and percentage<75):
   print("D")  
else :
    print("FAIL")

# Question 5 Program to accept price of 10 different itmes from user , Calculate Total .
# provide Discount on the basis of Total amount 
# if amount Exceed 2000 apply discount 20% , display discount and final amount . other wise no discount 
item_1 = int(input("Enter the price of item 1 : "))
item_2 = int(input("Enter the price of item 2 : "))
item_3 = int(input("Enter the price of item 3 : "))
item_4 = int(input("Enter the price of item 4 : "))
item_5 = int(input("Enter the price of item 5 : "))
item_6 = int(input("Enter the price of item 6 : "))
item_7 = int(input("Enter the price of item 7 : "))
item_8 = int(input("Enter the price of item 8 : "))
item_9 = int(input("Enter the price of item 9 : "))
item_10 = int(input("Enter the price of item 10 : "))
Total_amount = item_1+item_2+item_3+item_4+item_5+item_6+item_7+item_8+item_9+item_10
print(Total_amount)

if Total_amount>=2000:
    Discount = Total_amount/100*20
    print("Discount: ",Discount)
else:
    print("No Discount")
 
'''
Nesting :- placing one conditional construct inside another 
Types of Nesting 
1. If inside if 
Syntax if conditon:
         if condition:
             statement
         else:
         statement     

2. If inside  if else
3. if else inside if else
'''
 
#  qno.6 program to check number is +ve and even
n = int(input("Enter the number: "))

if n > 0:
    if n % 2 == 0:
        print("Number is +ve and even") 
    else:
        print("Number is +ve and odd")
else:
    if n < 0:
        if n % 2 == 0:
            print("Number is -ve and even") 
        else:
            print("Number is -ve and odd")
    else:
        print("Number is zero (neither positive nor negative)") 

   






