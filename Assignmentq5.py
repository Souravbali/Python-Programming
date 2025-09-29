# Write a program that takes marks in Physics, Chemistry, and Math.
# •	Calculate total and average.
# Admission Criteria:
# •	Average ≥ 70 and each subject ≥ 60 → "Eligible for Admission"
# •	Else if Math ≥ 90 → "Eligible under Math Special Quota"
# •	Else → "Not Eligible".
physics_marks = int(input("Enter the physics marks:"))
chemistry_marks = int(input("Enter the chemistry marks:"))
math_marks = int(input("Enter the math marks:"))
total_marks = (physics_marks+chemistry_marks+math_marks)
print(f"the total marks is {total_marks}")
average = (physics_marks+chemistry_marks+math_marks)/3
print(f"The average is {average}")
if average >= 70 and physics_marks >=60 and chemistry_marks >=60 and math_marks>=60:
   print("Eligible for addmission")
        
elif (math_marks>=90):
    print("Eligible under the math special quota:")


else:
    print("Not Eligible ")
