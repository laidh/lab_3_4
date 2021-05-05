from models import *
from managers import *


def main():
    dessert = Dishes("super Lunch", 2, 5000, Dish.COTTAGE_CHEESE, 500)
    shakes = Drinks("Triple Milkshake", 3, 800, Drink.MILK, 2)

    all_objects = [shakes, dessert]
    manager = ShopManager(all_objects)

    out = manager.sort_by_caloric(SortOrder.ASC)
    for i in out:
        print(i)
    print("___________________________________________________")
    print("\n")

    out = manager.sort_by_number_of_dishes(SortOrder.DESC)
    for i in out:
        print(i)
    print("___________________________________________________")
    print("\n")

    out = manager.search_by_number_of_dishes(3)
    for i in out:
        print(i)
    print("___________________________________________________")
    print("\n")


if __name__ == "__main__":
    main()
