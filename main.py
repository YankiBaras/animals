class Animal:
    def __init__(self, name, zoo_name="Hayaton"):
        self._name = name
        self._hunger = 0
        self._zoo_name = zoo_name

    def get_name(self):
        return self._name

    def is_hungry(self):
        if self._hunger > 0:
            return True
        else:
            return False

    def feed(self):
        self._hunger -= 1

    def talk(self):
        pass


class Dog(Animal):

    def __init__(self, name, hunger):
        super().__init__(name, hunger)

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):

    def __init__(self, name, hunger):
        Animal.__init__(self, name)
        self._hunger = hunger

    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):

    def __init__(self, name, hunger, stink_count=6):
        Animal.__init__(self, name)
        self._hunger = hunger
        self._stink_count = stink_count

    def talk(self):
        print("tssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):

    def __init__(self, name, hunger):
        Animal.__init__(self, name)
        self._hunger = hunger

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):

    def __init__(self, name, hunger, color="green"):
        Animal.__init__(self, name)
        self._hunger = hunger
        self._color = color

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


zoo_lst = []


def main():
    brownie = Dog("Brownie", 10)
    zelda = Cat("Zelda", 3)
    stinky = Skunk("Stinky", 0)
    keith = Unicorn("Keith", 7)
    lizy = Dragon("Lizzy", 1450)
    new_lst = [brownie, zelda, stinky, keith, lizy]
    for i in new_lst:
        zoo_lst.append(i)
    doggo = Dog("Doggo", 80)
    kitty = Cat("Kitty", 80)
    stinky = Skunk("Stinky jr.", 80)
    clair = Unicorn("Clair", 80)
    mcfly = Dragon("Mcfly", 80)
    new_lst2 = [doggo, kitty, stinky, clair, mcfly]
    for j in new_lst2:
        zoo_lst.append(j)

    for animal in zoo_lst:
        if animal.is_hungry() is True:
            print(animal.__class__.__name__, animal.get_name())
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        if isinstance(animal, Dog) is True:
            animal.fetch_stick()
        elif isinstance(animal, Cat) is True:
            animal.chase_laser()
        elif isinstance(animal, Skunk) is True:
            animal.stink()
        elif isinstance(animal, Unicorn) is True:
            animal.sing()
        elif isinstance(animal, Dragon) is True:
            animal.breath_fire()
    print(kitty._zoo_name)


main()
