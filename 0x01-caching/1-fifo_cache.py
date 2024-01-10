#!/usr/bin/env python3
"""
Implements FIFO caching algorithm
"""

BasicCaching = __import__('base_caching').BaseCaching


class FIFOCache(BasicCaching):
    """
    pop out first element in the cache system  when stack fills
    """

    def __init__(self):
        """initialize the child class"""
        super().__init__()

    def put(self, key, item):
        """put new item in the cache storage"""
        if key and item is not None:
            self.cache_data[key] = item
            if self.MAX_ITEMS < len(self.cache_data):
                keys = [keys for keys in self.cache_data.keys()]
                del self.cache_data[keys[0]]
                print('DISCARD: {}'.format(keys[0]))

    def get(self, key):
        """retrieve an item from the cache storage"""
        return self.cache_data.get(key)
