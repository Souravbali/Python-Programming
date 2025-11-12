class student:
    def __init__(self,name , id):
        self.name = name
        self.id = id 
    def display(self):
        print("Name:",self.name)
        print("Id:",self.id)
Student = student("Ram",1)
Student2 = student("shyam",2)
Student.display()
Student2.display()