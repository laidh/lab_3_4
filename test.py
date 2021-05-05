import unittest
from managers import *
from models import *


class TestShopManager(unittest.TestCase):

    def setUp(self):
        self.dessert = Dishes("super Lunch", 2, 5000, Dish.COTTAGE_CHEESE, 500)
        self.shakes = Drinks("Triple Milkshake", 3, 800, Drink.MILK, 2)

        all_objects = [self.shakes, self.dessert]
        self.manager = ShopManager(all_objects)

    def test_search_by_number_of_dishes(self):
        self.assertEqual(self.manager.search_by_number_of_dishes(3),
                         [self.shakes])

    def test_sort_by_number_of_dishes(self):
        self.assertEqual(
            self.manager.sort_by_number_of_dishes(SortOrder.DESC),
            [self.shakes, self.dessert]
        )

    def test_sort_by_caloric(self):
        self.assertEqual(
            self.manager.sort_by_caloric(SortOrder.ASC),
            [self.shakes, self.dessert]
        )


if __name__ == "__main__":
    unittest.main()
