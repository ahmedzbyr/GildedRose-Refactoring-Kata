# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    
    #
    # All other items 
    #   - Once the sell by date has passed, quality degrades twice as fast
    #   - The quality of an item is never negative.
    #   - The quality of an item is never more than 50
    #
    def test_all_other_items_1(self):
        items = [Item("all_other_items", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("all_other_items", items[0].name) 
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(9, items[0].quality)

    def test_all_other_items_2(self):
        items = [Item("all_other_items", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("all_other_items", items[0].name) 
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(0, items[0].quality)   

    def test_all_other_items_3(self):
        items = [Item("all_other_items", 0, 12)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("all_other_items", items[0].name) 
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(10, items[0].quality) 

    def test_all_other_items_4(self):
        items = [Item("all_other_items", -1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("all_other_items", items[0].name) 
        self.assertEquals(-2, items[0].sell_in)
        self.assertEquals(0, items[0].quality) 

    #
    # Aged Brie 
    #   - "Aged Brie" actually increases in quality the older it gets
    #   -  The quality of an item is never more than 50
    #
    def test_aged_brie_1(self):
        items = [Item("Aged Brie", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name) 
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(11, items[0].quality)

    def test_aged_brie_2(self):
        items = [Item("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name) 
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(2, items[0].quality)   

    def test_aged_brie_3(self):
        items = [Item("Aged Brie", 0, 12)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name) 
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(14, items[0].quality) 

    def test_aged_brie_4(self):
        items = [Item("Aged Brie", -1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name) 
        self.assertEquals(-2, items[0].sell_in)
        self.assertEquals(2, items[0].quality) 

    def test_aged_brie_5(self):
        items = [Item("Aged Brie", -1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name) 
        self.assertEquals(-2, items[0].sell_in)
        self.assertEquals(50, items[0].quality)         

    #
    # - "Sulfuras", being a legendary item, never has to be sold or decreases in quality
    #
    def test_sulfuras_1(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Sulfuras, Hand of Ragnaros", items[0].name) 
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(50, items[0].quality)  

    def test_sulfuras_2(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Sulfuras, Hand of Ragnaros", items[0].name) 
        self.assertEquals(5, items[0].sell_in)
        self.assertEquals(10, items[0].quality) 

    def test_sulfuras_3(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 100, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Sulfuras, Hand of Ragnaros", items[0].name) 
        self.assertEquals(100, items[0].sell_in)
        self.assertEquals(1, items[0].quality)                 

    #   
    # - "Backstage passes", like aged brie, increases in quality as its sell-in
    #       value approaches; quality increases by 2 when there are 10 days or less
    #       and by 3 when there are 5 days or less but quality drops to 0 after the
    #       concert
    #
    def test_backstage_passes_1(self):
        # quality increases by 2 when there are 10 days or less
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name) 
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(12, items[0].quality)  

    def test_backstage_passes_2(self):
        # by 3 when there are 5 days or less 
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name) 
        self.assertEquals(4, items[0].sell_in)
        self.assertEquals(13, items[0].quality)  

    def test_backstage_passes_3(self):
        # but quality drops to 0 after the concert
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name) 
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(0, items[0].quality)  

    def test_backstage_passes_4(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name) 
        self.assertEquals(4, items[0].sell_in)
        self.assertEquals(50, items[0].quality)  

    def test_backstage_passes_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name) 
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(50, items[0].quality)  

    #
    # "Conjured" items degrade in quality twice as fast as normal items
    #

    def test_conjured_1(self):
        items = [Item("Conjured Mana Cake", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Conjured Mana Cake", items[0].name) 
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(48, items[0].quality) 

    def test_conjured_2(self):
        items = [Item("Conjured Mana Cake", 8, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Conjured Mana Cake", items[0].name) 
        self.assertEquals(7, items[0].sell_in)
        self.assertEquals(0, items[0].quality)         

if __name__ == '__main__':
    unittest.main()
