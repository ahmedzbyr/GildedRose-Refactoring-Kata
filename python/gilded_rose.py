# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:
            if item.name == "Aged Brie":
                self.aged_brie(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.sulfuras(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.backstage_pass(item)
            elif  item.name == "Conjured Mana Cake":
                self.conjured(item)   
            else:
                self.all_other_items(item)

    #
    # "Conjured" items degrade in quality twice as fast as normal items
    #  Very similar to method `all_other_items`, just the quantity is reduced twice as much. 
    #
    def conjured(self, item):
        
        # WE always reduce the sell_in days.
        item.sell_in -= 1

        # If the quantity is zero then we return the item nothing to do here. 
        if item.quality <= 0:
            item.quality = 0
            return item 

        # If we have enough quntity then reduce it.
        item.quality -= 2

        # If we have less= 0 sell_in days then we reduce quantity by one more. 
        if item.sell_in <= 0 and not item.quality <= 0:
            item.quality -= 2 

        # return what we have.     
        return item 

    #
    # Sulfuras
    #
    def sulfuras(self, item):
        # - "Sulfuras", being a legendary item, never has to be sold or decreases in quality
        return item 

    #
    # Backstage Pass
    #   
    def backstage_pass(self, item):
        # We always reduce the sell_in days.
        item.sell_in -= 1 

        # Increment the quantity by one
        if item.quality < 50:
            item.quality += 1
        
        # when we reach the sell_in to 0 then we have zero quantity. 
        if item.sell_in <= 0:
            item.quality = 0
            return item 

        # When we reach the 10day mark then we increment by one. [2 times here]
        if item.sell_in <= 10 and item.quality < 50:
            # Increment the quantity by one
            item.quality += 1

        # When are at 5 day mark we increment by one more. [3 times here ]
        if item.sell_in <= 5 and item.quality < 50:
            # Increment the quantity by one
            item.quality += 1
        
        return item 

    #
    # Aged Brie
    #
    def aged_brie(self, item):
        # WE always reduce the sell_in days.
        item.sell_in -= 1
        
        # Increment the quality by one
        if item.quality < 50:
            item.quality += 1

        # If we are less than the sell_in dates then we go up in quality but not to exceed 50
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1
    
        return item

    #
    # All normal items
    #
    def all_other_items(self, item):
        
        # WE always reduce the sell_in days.
        item.sell_in -= 1

        # If the quality is zero then we return the item nothing to do here. 
        if item.quality <= 0:
            item.quality = 0
            return item 

        # If we have enough quality then reduce it.
        item.quality -= 1

        # If we have less= 0 sell_in days then we reduce quality by one more. 
        if item.sell_in <= 0 and not item.quality <= 0:
            item.quality -= 1 

        # return what we have.     
        return item 

        


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "{:<45} {:<10} {:<10}".format(self.name, self.sell_in, self.quality)
