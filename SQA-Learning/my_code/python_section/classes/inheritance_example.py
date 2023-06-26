class MyClass1:
    def __init__(self):
        print("__init__ of class 1")
        self.prpcls1 = 10

    def method_1_class(self):
        print("method_1_class_1")


class MyClas2:
    pass


obj1 = MyClass1()
obj1.method_1_class()

obj2 = MyClas2()
