#!/usr/bin/python3
""" class LFUCache that inherits from BaseCaching and is a caching system """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - Inherits from BaseCaching
      - Caching system
    """

    def __init__(self):
        """
        Initialize the LFU cache.
        """
        super().__init__()
        self.usage_count = {}  # To track the usage count of items
        self.lfu_keys = []  # To track the least frequently used keys

    def put(self, key, item):
        """
        Add an item to the cache using LFU algorithm.
        If key or item is None, do nothing.
        If the cache is full, discard the least frequently used item.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least frequently used item
                lfu_key = self.lfu_keys.pop(0)
                print("DISCARD: {}".format(lfu_key))
                del self.cache_data[lfu_key]
                del self.usage_count[lfu_key]
            self.cache_data[key] = item
            self.usage_count[key] = 0
            self.lfu_keys.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.
        If key is None or not in cache_data, return None.
        """
        if key in self.cache_data:
            # Increment the usage count of the accessed key
            self.usage_count[key] += 1
            # Update the least frequently used keys
            self.lfu_keys.sort(key=lambda k: (self.usage_count[k], k))
        return self.cache_data.get(key)
