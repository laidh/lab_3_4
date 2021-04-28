from .breakfast import Breakfast


class Drinks(Breakfast):
    def __init__(self, name, number_of_dishes, caloric,
                 drink):
        Breakfast.__init__(self, name, number_of_dishes, caloric)
        self.__drink = drink

    def __str__(self):
        return f"In drink {self._name} there are "\
              f"{self.number_of_dishes} dishes.\nAverage caloric is "\
              f"{self._caloric}.\nhe name of the dish is "\
              f"{self.__drink.name}."\
              f"\n"\


    def get_drink(self):
        return self.__drink

    def set_drink(self, drink):
        self.__drink = drink
