class Dog:
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def eat(self):
        print("Dog eat......")

    def bark(self):
        print("woofff")

    def breath(self):
        print("breath")

    def as_security(self):
        print("My dog is my home security")


class Cat:

    def __init__(self, breat, name):
        self.breat = breat
        self.name = name

    def eat(self):
        print("Eat_____")

    def meaw(self):
        print("meeewwww")


mydog = Dog('Buldog', 'Max')
print(mydog.breed)
print(mydog.name)
mydog.eat()

mycat = Cat('test', 'wwww')
mycat.eat()
mycat.meaw()
