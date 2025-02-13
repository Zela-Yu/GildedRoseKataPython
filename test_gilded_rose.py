# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from gilded_rose import Item, NormalItem


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    # def test_sulfuras_should_not_decrease_quality(self):
    #     items = [Item("Sulfuras", 5, 80)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     sulfuras_item = items[0]
    #     self.assertEqual(80, sulfuras_item.quality)
    #     self.assertEqual(4, sulfuras_item.sell_in)
    #     self.assertEqual("Sulfuras", sulfuras_item.name)

    # # example of test that checks for syntax errors
    # def test_gilded_rose_list_all_items(self):
    #     items = [Item("Sulfuras", 5, 80)]
    #     gilded_rose = GildedRose(items)
    #     all_items = gilded_rose.get_item()
    #     self.assertEqual(["Sulfuras"], all_items)

    def test_normal_item(self):
        item = Item("Normal Item", 10, 20)
        normal = NormalItem(item)
        normal.update()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 19)

if __name__ == '__main__':
    unittest.main()
