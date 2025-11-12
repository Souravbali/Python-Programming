class animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")

    def findname(self):
        return self.name

obj = animal('billi')
print(obj.name)  # Output: billi

class cat:
    def __init__(self, name, breed):
        self.name = name          # <-- added: initialize 'name'
        self.breed = breed

    def flying(self):
        print(self.name, "is flying")

Cat = cat('kity', 'british')    # Create a 'cat' object with name and breed

class tiger(animal, cat):
    def __init__(self, name, breed, power):
        animal.__init__(self, name)   # Explicitly call parent initializers
        cat.__init__(self, name, breed)
        self.power = power

    def hunting(self):
        print("Tiger is hunting")

Tiger = tiger('Sheru', 'Bengal', 'Strong')  # Pass all required arguments
Tiger.eat()            # Output: Sheru is eating
Tiger.flying()         # Output: Sheru is flying
Tiger.hunting()        # Output: Tiger is hunting
print(Tiger.power)     # Output: Strong
