#!/usr/bin/env python3
"""
Implements FIFO caching algorithm
"""
from collections import OrderedDict
BasicCaching = __import__('base_caching').BaseCaching


class LRUCache(BasicCaching):
    """
    pop out first element in the cache system  when stack fills
    """

    def __init__(self):
        """initialize the child class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """add new item in the ordered dictionary"""
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

            if len(self.cache_data) > self.MAX_ITEMS:
                lru_key = self.cache_data.popitem(last=True)
                print('DISCARD: {}'.format(lru_key[0]))

    def get(self, key):
        """retrieve an item from the cache storage"""
        if self.cache_data.get(key) is not None:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key)
