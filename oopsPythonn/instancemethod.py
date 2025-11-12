class person:
    country = 'india'
    @classmethod
    def greet(cls):  # class method
        print("hello",cls.country) 
    def __init__(self,name, age ):
        self.name = name 
        self.age = age 

    def findage(self):
        return self.age # instance method

    def hello(self):  # static method , it is independent of properties of object and class 
        print("hello world ",)
per = person('sourav',24)
print(per.findage())
per.greet()
per.hello()
