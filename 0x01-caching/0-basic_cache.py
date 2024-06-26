#!/usr/bin/python3
""" Basic dictionary """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - Inherits from BaseCaching
      - Caching system
    """

    def put(self, key, item):
        """
        Add an item to the cache.
        If key or item is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.
        If key is None or not in cache_data, return None.
        """

        return self.cache_data.get(key)
