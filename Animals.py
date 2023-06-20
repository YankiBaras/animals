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

