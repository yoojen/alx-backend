#!/usr/bin/env python3
"""
Implement basic caching system
"""

BasicCaching = __import__('base_caching').BaseCaching


class BasicCache(BasicCaching):
    """implement basic caching algorithm"""

    def put(self, key, item):
        """put new item in the cache storage"""
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """retrieve an item from the cache storage"""
        return self.cache_data.get(key)
