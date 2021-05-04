from abc import ABC


class Breakfast(ABC):

    def __init__(self, name, number_of_dishes, caloric):
        self._name = name
        self.number_of_dishes = number_of_dishes
        self._caloric = caloric

    def __str__(self):
        pass

    def get_name(self):
        return self._name

    def set_name(self, _name):
        self._name = _name

    def get_caloric(self):
        return self._caloric

    def set_caloric(self, _caloric):
        self._caloric = _caloric
