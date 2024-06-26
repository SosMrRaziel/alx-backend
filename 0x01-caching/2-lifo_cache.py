#!/usr/bin/python3
""" LIFO Caching """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - Inherits from BaseCaching
      - Caching system
    """

    def __init__(self):
        """
        Initialize the LIFO cache.
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Add an item to the cache using LIFO algorithm.
        If key or item is None, do nothing.
        If the cache is full, discard the last item added (LIFO).
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the last item (LIFO)
                last_key = self.keys.pop()
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.
        If key is None or not in cache_data, return None.
        """
        return self.cache_data.get(key)
