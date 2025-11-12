class animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name," is eating")
    def findname(self):
        return self.name

obj = animal('billi')
print(obj.name)  # Output: billi

class cat(animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

Cat = cat('kity', 'british')  # Provide both name and breed
print(obj.name)   # Output: kity
print(Cat.breed)  # Output: british
Cat.eat()
print(Cat.findname())
class rat(cat):
    def __init__(self,name,breed,speed):
        super().__init__(name,breed)
        self.speed = speed
Rat = rat('mouse','small',45)
print(Rat.name)
Rat.eat()