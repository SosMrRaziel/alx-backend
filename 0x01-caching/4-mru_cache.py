#!/usr/bin/python3
""" class MRUCache that inherits from BaseCaching and is a caching system """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines:
      - Inherits from BaseCaching
      - Caching system
    """

    def __init__(self):
        """
        Initialize the MRU cache.
        """
        super().__init__()
        self.usage_order = []  # To track the order of item usage

    def put(self, key, item):
        """
        Add an item to the cache using MRU algorithm.
        If key or item is None, do nothing.
        If the cache is full, discard the most recently used item (MRU).
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the most recently used item (MRU)
                mru_key = self.usage_order.pop()
                print("DISCARD: {}".format(mru_key))
                del self.cache_data[mru_key]
            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.
        If key is None or not in cache_data, return None.
        """
        if key in self.cache_data:
            # Move the accessed key to the end of the usage order
            self.usage_order.remove(key)
            self.usage_order.append(key)
        return self.cache_data.get(key)
