# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from gilded_rose import Item, NormalItem, AgedBrie, BackstagePass, Sulfuras


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

    def test_normal_item_expired(self):
        item = Item("Normal Item", 0, 10)
        normal = NormalItem(item)
        normal.update()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 8) 

    def test_aged_brie(self):
        item = Item("Aged Brie", 5, 10)
        brie = AgedBrie(item)
        brie.update()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 11)

    def test_aged_brie_expired(self):
        item = Item("Aged Brie", 0, 10)
        brie = AgedBrie(item)
        brie.update()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 12)

    def test_backstage_pass_high_sell_in(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
        pass_item = BackstagePass(item)
        pass_item.update()
        self.assertEqual(item.sell_in, 14)
        self.assertEqual(item.quality, 21)

    def test_backstage_pass_mid_sell_in(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)
        pass_item = BackstagePass(item)
        pass_item.update()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 22)

    def test_backstage_pass_low_sell_in(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)
        pass_item = BackstagePass(item)
        pass_item.update()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 23)

    def test_backstage_pass_expired(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
        pass_item = BackstagePass(item)
        pass_item.update()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 0)

    def test_sulfuras(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 80)
        sulfuras = Sulfuras(item)
        sulfuras.update()
        self.assertEqual(item.sell_in, 5)
        self.assertEqual(item.quality, 80) 

if __name__ == '__main__':
    unittest.main()
