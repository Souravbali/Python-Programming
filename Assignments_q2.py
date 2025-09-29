# Q2. Loan Eligibility System
# Create a program that checks loan eligibility.
# Inputs: age, monthly_income, existing_loan, CIBIL_score.
# Conditions:
# •	Age must be between 21–60
# •	Income must be ≥ 25,000
# •	Existing loan must be ≤ 50% of income
# •	CIBIL score ≥ 700
# If all conditions are satisfied → "Eligible for Loan"
# Else, display reason for rejection (e.g., "Rejected due to low CIBIL score").
age = int(input("Enter age:"))
Monthly_income = int(input("Enter Monthly income:"))
Existing_loan = int(input("Enter the existing loan:"))
cibil_score = int(input("Enter the cibil score:"))

if age>=21 and age<=60 and Monthly_income>=25000 and Existing_loan <= 0.5*Monthly_income  and cibil_score >= 700:
    print("All conditions are satisfied -> eligible for loan")

else:
    print("Rejected -> not eligible for loan")