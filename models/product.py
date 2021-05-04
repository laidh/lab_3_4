from .breakfast import Breakfast


class Product(Breakfast):
    def __init__(self, name, number_of_dishes, caloric, fatness,
                    producer_names):
        Breakfast.__init__(self, name, number_of_dishes, caloric)
        self.__fatness = fatness
        self.__producer_names = producer_names

    def __str__(self):
        return f"In Product {self._name} there are " \
               f"{self.number_of_dishes} dishes.\nAverage caloric is " \
               f"{self._caloric}.\nHere are the names of producer: " \
               f"{self.__producer_names}"\
               f"\n"\


    def get_fatness(self):
        return self.__fatness

    def set_fatness(self, fatness):
        self.__fatness = fatness

    def get_producer_names(self):
        return self.__producer_names

    def set_producer_names(self, producer_names):
        self.__producer_names = producer_names
