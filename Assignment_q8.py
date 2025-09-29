# Q8. ATM Transaction Simulation
# Inputs: account_balance, amount_to_withdraw, account_type (Saving/Current), day (weekday/weekend).
# Rules:
# •	Withdrawal allowed only if balance ≥ withdrawal + 1000 (minimum balance).
# •	Weekend transactions charge extra ₹50 fee.
# •	Saving account daily limit = 25,000; Current account = 50,000.
# Output: Success/Failure with reason and updated balance

Account_balance = int(input("Enter the account balance:"))
Amount_withdraw = int(input("Enter the withdraw amount:"))
Account_type = input("Enter the Account_type:")
day = input("Enter the day (weekday/weekend):")


if Account_balance < Amount_withdraw +  1000:
    print("Failure: Cannot maintain minimum balance of ₹1000")
    exit()

if Account_type == "Saving":
    if Amount_withdraw <= 25000:
        Account_balance = Account_balance - Amount_withdraw
        if day == "weekend":
            Account_balance = Account_balance - 50
        print("Transaction successful")
    else:
        print("Failure: Saving account limit exceeded (₹25,000)")

elif Account_type == "Current":
    if Amount_withdraw <= 50000:
        Account_balance = Account_balance - Amount_withdraw
        if day == "weekend":
            Account_balance =Account_balance - 50
        print("Transaction successful")
    else:
        print("Failure: Current account limit exceeded (₹50,000)")

else:
    print("Transaction failed: Invalid account type")

print("Updated balance:", Account_balance)