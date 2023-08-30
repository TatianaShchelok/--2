class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def getname(self):
        return self.name

    def getgender(self):
        return self.gender

    def getage(self):
        return self.age
      
from Cat import Cat

Sam = Cat("Сэм", "Мальчик", "2 года")
Baron = Cat("Барон", "Мальчик", "2 года")
print(Sam)
print(Baron)
