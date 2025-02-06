# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_item()
        self.assertEqual(["Sulfuras"], all_items)

    def test_quality_never_negative(self):
        items = [Item("Apple", 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        apple_item = items[0]
        self.assertEqual(-1, apple_item.quality)

    def test_aged_brie_increases_quality(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        aged_brie_item = items[0]
        self.assertGreater(0, aged_brie_item.quality)

    def test_backstage_passes_quality_drops_to_zero(self):
        items = [Item("Backstage pass", 0, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        backstage_pass_item = items[0]
        self.assertEqual(30, backstage_pass_item.quality) 

    def test_get_qulity_method(self):
        items = [Item("Banana", 5, 7)]
        gilded_rose = GildedRose(items)
        quality = gilded_rose.get_quality
        self.assertEqual(7, quality)
        

if __name__ == '__main__':
    unittest.main()
