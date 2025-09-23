# Write a program to input the marks of 5 subjects and then calculate
#  Total Marks Obtained
#  Percentage of Marks
#  Display grade
Social_science=int(input("Enter the social_science marks:"))
Science = int(input("Enter the  science marks: "))
Hindi = int(input("Enter the hindi marks: "))
Math = int(input("Enter the math marks: "))
English = int(input("Enter the English: "))
Total_marks = int(input("Enter the total marks:"))
Marks_obtain = (Social_science+Science+Hindi+Math+English)
print("Marks obtain: ",Marks_obtain)
Marks_percentage = (Marks_obtain/Total_marks)*100
print("marks percentage: ",Marks_percentage)
if (Marks_percentage>100) or (Marks_percentage>=0):
    print("invalid percentage")
elif Marks_percentage >= 95:
    print("Grade A")
elif Marks_percentage >= 85 and Marks_percentage < 95:
    print("Grade B")
elif Marks_percentage >= 70 and Marks_percentage < 85:
    print("Grade C")
elif Marks_percentage >= 60 and Marks_percentage < 70:
    print("Grade D")
else:
    print("Fail !!oops not qualified")