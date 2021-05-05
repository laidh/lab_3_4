class ShopManager:

    def __init__(self, recipes):
        self.__recipes = recipes

    def search_by_number_of_dishes(self, number=0):
        output = list()
        for i in self.__recipes:
            if i.number_of_dishes == number:
                output.append(i)
        return output

    def sort_by_number_of_dishes(self, order):
        self.__recipes.sort(key=lambda c: c.number_of_dishes,
                               reverse=bool(order.value))
        return self.__recipes

    def sort_by_caloric(self, order):
        self.__recipes.sort(key=lambda c: c.get_caloric(),
                               reverse=bool(order.value))
        return self.__recipes
