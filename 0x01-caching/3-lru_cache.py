#!/usr/bin/python3
""" a class LRUCache that inherits from BaseCaching and is a caching system """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines:
      - Inherits from BaseCaching
      - Caching system
    """

    def __init__(self):
        """
        Initialize the LRU cache.
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        Add an item to the cache using LRU algorithm.
        If key or item is None, do nothing.
        If the cache is full, discard the least recently used item.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the least recently used item
                lru_key = self.usage_order.pop(0)
                print("DISCARD: {}".format(lru_key))
                del self.cache_data[lru_key]
            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.
        If key is None or not in cache_data, return None.
        """
        if key in self.cache_data:
            self.usage_order.remove(key)
            self.usage_order.append(key)
        return self.cache_data.get(key)
