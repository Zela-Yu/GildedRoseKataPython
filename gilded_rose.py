# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Updater:
    def __init__(self, item: Item):
        self.item = item

    @abstractmethod
    def update(self):
        pass

    def decrease_quality(self, amount=1):
        if self.item.quality > 0:
            self.item.quality = max(0, self.item.quality - amount)

    def increase_quality(self, amount=1):
        if self.item.quality < 50:
            self.item.quality = min(50, self.item.quality + amount)

    def decrease_sell_in(self):
        self.item.sell_in -= 1

class NormalItem(Updater):
    def update(self):
        self.decrease_quality()
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.decrease_quality()

class AgedBrie(Updater):
    def update(self):
        self.increase_quality()
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.increase_quality()

class BackstagePass(Updater):
    def update(self):
        if self.item.sell_in > 10:
            self.increase_quality()
        elif self.item.sell_in > 5:
            self.increase_quality(2)
        elif self.item.sell_in > 0:
            self.increase_quality(3)
        else:
            self.item.quality = 0
        self.decrease_sell_in()

class Sulfuras(Updater):
    def update(self):
        pass

ITEM_CLASSES = {
    "Aged Brie": AgedBrie,
    "Backstage passes to a TAFKAL80ETC concert": BackstagePass,
    "Sulfuras, Hand of Ragnaros": Sulfuras,
}

class GildedRose(object):
    
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater_class = ITEM_CLASSES.get(item.name, NormalItem)
            updater_class(item).update()
