from .breakfast import Breakfast


class Dishes(Breakfast):
    def __init__(self, name, number_of_dishes, caloric,
                 dish,):
        Breakfast.__init__(self, name, number_of_dishes, caloric)
        self.__dish = dish

    def __str__(self):
        return f"In dish {self._name} there are "\
              f"{self.number_of_dishes} dishes.\nAverage caloric is "\
              f"{self._caloric}.\nThe name of the dish is "\
              f"{self.__dish}."\
              f"\n"\


    def get_dish(self):
        return self.__dish

    def set_dish(self, dish):
        self.__dish = dish
