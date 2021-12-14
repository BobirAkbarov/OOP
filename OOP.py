class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name,  "Im " f"{self.age} " "years old")

p1 = Person("Bobir", 20)
p1.myfunc()