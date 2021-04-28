from models import *
from managers import *


def main():
    a = Dishes("lunch", 2, 5000, Dish.COTTAGE_CHEESE)
    b = Product("lunch", 1, 1000, 5, "Dobryana")
    c = Drinks("lunch", 3, 800, Drink.MILK,)

    l_dbac = [b, c, a]
    f = ShopManager(l_dbac)

    out = f.sort_by_caloric(SortOrder.ASC)
    for i in out:
        print(i)
    print("___________________________________________________")
    print("\n")

    out = f.sort_by_number_of_dishes(SortOrder.DESC)
    for i in out:
        print(i)
    print("___________________________________________________")
    print("\n")

    out = f.search_by_number_of_dishes(3)
    for i in out:
        print(i)
    print("___________________________________________________")
    print("\n")


if __name__ == "__main__":
    main()
