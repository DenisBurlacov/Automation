class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def move(self):
        print("animal move")

    def eat(self):
        print('Animal eat')

    def breath(self):
        print("Animal breath")


class Cats(Animal):
    pass


class Dogs(Animal):
    pass


cat = Cats('Kasper', 4)
print(cat)

dog = Dogs('Metr', 6)
print(dog.name)

dog.eat()
