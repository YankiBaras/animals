class Animal:
    count_animals = 0

    def __init__(self, name):
        Animal.count_animals += 1
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)


mitzy = Cat("Mitzy")
citty = Cat("Kitty")
michel = Cat("Michel")

bella = Dog("Bella")
charlie = Dog("Charlie")
luna = Dog("Luna")

print(Animal.count_animals)
