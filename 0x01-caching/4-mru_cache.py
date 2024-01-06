#!/usr/bin/env python3
"""
Implements FIFO caching algorithm
"""
from collections import OrderedDict
BasicCaching = __import__('base_caching').BaseCaching


class MRUCache(BasicCaching):
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
            if key not in self.cache_data:
                if len(self.cache_data) == self.MAX_ITEMS:
                    mru_key = self.cache_data.popitem(last=False)
                    print('DISCARD: {}'.format(mru_key[0]))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """retrieve an item from the cache storage"""
        if self.cache_data.get(key) is not None:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key)
