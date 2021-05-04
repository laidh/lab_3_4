from .breakfast import Breakfast


class Drinks(Breakfast):
    def __init__(self, name, number_of_dishes, caloric,
                 drink, volume):
        Breakfast.__init__(self, name, number_of_dishes, caloric)
        self.__drink = drink
        self.__volume = volume

    def __str__(self):
        return f"In drink {self._name} there are "\
              f"{self.number_of_dishes} drinks.\nAverage caloric is "\
              f"{self._caloric}.\nhe name of the drink is "\
              f"{self.__drink.name}. \nAnd volume: "\
              f"{self.__volume} litres."\
              f"\n"\


    def get_drink(self):
        return self.__drink

    def set_drink(self, drink):
        self.__drink = drink

    def get_volume(self):
        return self.__volume

    def set_volume(self, volume):
        self.__volume = volume
