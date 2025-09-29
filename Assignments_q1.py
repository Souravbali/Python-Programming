# Q1. Employee Salary Slip Generator
# Write a program that accepts basic salary of an employee and calculate the following:
# •	HRA = 20% of basic
# •	DA = 10% of basic
# •	PF = 12% of basic
# •	Gross Salary = Basic + HRA + DA
# •	Net Salary = Gross – PF
# Decision Rules:
# •	If Net Salary ≥ 80,000 → Category = "High Earner"
# •	If 50,000 ≤ Net Salary < 80,000 → "Mid Earner"
# •	Else → "Low Earner
basic_salary = int(input("Enter the basic salary:"))
hra = (20/100)*basic_salary
print(f"HRA:{hra}")
da = (10/100)*basic_salary
print(f"DA:{da}")
pf = (12/100)*basic_salary
print(f"PF:{pf}")
Gross_salary = basic_salary+hra+da
print(f"Gross salary:{Gross_salary}")
Net_salary = Gross_salary-pf
print(f"Net salary:{Net_salary}")

if Net_salary>=80000:
    print("High earner")

elif Net_salary>=50000 and Net_salary<80000:
    print("Mid Earner")

else:
    print("Low earner")