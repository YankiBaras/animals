from Animals import Animal
from Dogs import Dog
from Cats import Cat
from Skunks import Skunk
from Unicorns import Unicorn
from Dragons import Dragon


def main():
    zoo_lst = []

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
