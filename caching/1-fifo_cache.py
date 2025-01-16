#!/usr/bin/env python3


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache - First In, First Out
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        # list to keep track of the order of keys
        self.order = []

    def put(self, key, item):
        """adding item to the cache"""
        if key is None or item is None:
            return

        # If the key already exists, remove it from the order list
        if key in self.cache_data:
            self.order.remove(key)

        # Adding the key value pair to the cache
        self.cache_date[key] = item
        # Tracking the in FIFO order
        self.order.append(key)

        # Check if the cache has exceeded max length
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the first key added (FIFO)
            discarded_key = self.order.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """Get data from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
