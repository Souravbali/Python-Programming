# Q7. Online Examination Result
# Inputs: Correct answers, Wrong answers, Unattempted.
# Marking scheme: +4 for correct, –1 for wrong, 0 for unattempted.
# Rules:
# •	Score ≥ 180 → "Excellent"
# •	120–179 → "Good"
# •	60–119 → "Average"
# •	Below 60 → "Fail"
# Also, if Wrong answers > Correct answers, show: "Improve accuracy!"
Total_ans = int(input("Enter the total ans:"))
correct_ans = int(input("Enter the correct answere:"))
wrong_ans = int(input("Enter the wrong answere:"))
unattempted_ans = int(input("Enter the unattempted answere:"))
if Total_ans ==(correct_ans+wrong_ans+unattempted_ans):
   correctans_mark = 4*correct_ans
   wrongans_mark = (-1)*wrong_ans
   unattempted_ansmark = 0
   Score = (correctans_mark+wrongans_mark+unattempted_ansmark)
else:
   print("please Enter the total ans correct:")
   exit()

if Score>=180:
   print("Excellent")

elif Score>=120 and Score<=179:
   print("Good")

elif Score>=60 and Score<=119:
   print("Average")

else:
   print("Fail")

if wrong_ans>correct_ans:
   print("Improve your accuracy")