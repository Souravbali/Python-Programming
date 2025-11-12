class calculator:
    def add(self , a , b , c= 0,d=0 ):
        return a+b+c
cal = calculator()
print(cal.add(5,6,7))
print(cal.add(5,6))
print(cal.add(5,6,7,8))