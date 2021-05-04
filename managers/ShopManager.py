class ShopManager:

    def __init__(self, breakfasts):
        self.__breakfasts = breakfasts

    def search_by_number_of_dishes(self, number=0):
        output = list()
        for i in self.__breakfasts:
            if i.number_of_dishes == number:
                output.append(i)
        return output

    def sort_by_number_of_dishes(self, order):
        self.__breakfasts.sort(key=lambda c: c.number_of_dishes,
                               reverse=bool(order.value))
        return self.__breakfasts

    def sort_by_caloric(self, order):
        self.__breakfasts.sort(key=lambda c: c.get_caloric(),
                               reverse=bool(order.value))
        return self.__breakfasts
