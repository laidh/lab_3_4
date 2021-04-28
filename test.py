import unittest
from managers import *
from models import *


class TestShopManager(unittest.TestCase):

    def setUp(self):
        self.a = Dishes("lunch", 2, 5000, Dish.COTTAGE_CHEESE)
        self.b = Product("lunch", 1, 1000, 5, "Dobryana")
        self.c = Drinks("lunch", 3, 800, Drink.MILK, )
        result = [self.b, self.c, self.a]

        self.shopManager = ShopManager(result)
        self.maxDiff = None

    def test_search_by_number_of_dishes(self):
        self.assertEqual(self.shopManager.search_by_number_of_dishes(3),
                         [self.c])

    def test_sort_by_number_of_dishes(self):
        self.assertEqual(
            self.shopManager.sort_by_number_of_dishes(SortOrder.DESC),
            [self.c, self.a, self.b]
        )

    def test_sort_by_caloric(self):
        self.assertEqual(
            self.shopManager.sort_by_caloric(SortOrder.ASC),
            [self.c, self.b, self.a]
        )


if __name__ == "__main__":
    unittest.main()
