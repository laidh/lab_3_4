from .breakfast import Breakfast


class Dishes(Breakfast):
    def __init__(self, name, number_of_dishes, caloric,
                 dish, mass):
        Breakfast.__init__(self, name, number_of_dishes, caloric)
        self.__dish = dish
        self.__mass = mass

    def __str__(self):
        return f"In dish {self._name} there are "\
              f"{self.number_of_dishes} dishes.\nAverage caloric is "\
              f"{self._caloric}.\nThe name of the dish is "\
              f"{self.__dish}. \nAnd mass: "\
              f"{self.__mass} grams."\
              f"\n"\


    def get_dish(self):
        return self.__dish

    def set_dish(self, dish):
        self.__dish = dish

    def get_mass(self):
        return self.__mass

    def set_mass(self, mass):
        self.__mass = mass
