
# Example Student Mnangement System using Functions 
#Example Student Management System using Functions
def Welcome():
    print("Welcome")

def Validate_Registration(reg):
    if reg>=1 and reg<=200:
        print("Registration Number is Valid")
        return "Valid"
    else:
        print("Registration Number is not Valid")
        return "Not Valid"

def Login(status):
    if status=="Valid":
        print("You are Successfully Login")
    else:
        print("Login Failed")

Welcome()
Regg = int(input("Enter Your Registration Number"))
res = Validate_Registration(Regg)
Login(res)

