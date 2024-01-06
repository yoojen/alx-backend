#!/usr/bin/env python3
"""
Implements FIFO caching algorithm
"""

BasicCaching = __import__('base_caching').BaseCaching


class LIFOCache(BasicCaching):
    """
    pop out first element in the cache system  when stack fills
    """

    def __init__(self):
        """initialize the child class"""
        self.__recent_updated = []
        super().__init__()

    def put(self, key, item):
        """update the lifo stack
        args:
            key: key that holds value in the lifo dict
            item: item to be assigned to value in dict
        """
        self.__recent_updated.append(key)
        if key and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                del self.cache_data[self.__recent_updated[-2]]
                print('DISCARD: {}'.format(self.__recent_updated[-2]))

    def get(self, key):
        """retrieve an item from the cache storage"""
        return self.cache_data.get(key)
