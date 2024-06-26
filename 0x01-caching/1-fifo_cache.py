#!/usr/bin/python3
"""class FIFOCache that inherits from BaseCaching and is a caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class"""
    def __init__(self):
        """
        Initialize the FIFO cache.
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Add an item to the cache using FIFO algorithm.
        If key or item is None, do nothing.
        If the cache is full, discard the first item added (FIFO).
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the first item (FIFO)
                first_key = next(iter(self.cache_data))
                print("DISCARD: {}".format(first_key))
                del self.cache_data[first_key]
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.
        If key is None or not in cache_data, return None.
        """
        return self.cache_data.get(key)
