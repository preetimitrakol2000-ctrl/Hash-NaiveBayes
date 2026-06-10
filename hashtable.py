class NodeItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class CustomHashTable:
    """Singly linked list lookup chaining table to manage O(1) text tokens."""
    def __init__(self, size=100):
        self.size = size
        self.buckets = [None] * size

    def _hash_function(self, key):
        hash_val = 5381
        for char in key:
            hash_val = ((hash_val << 5) + hash_val) + ord(char)
        return hash_val % self.size

    def put(self, key, value):
        idx = self._hash_function(key)
        if not self.buckets[idx]:
            self.buckets[idx] = NodeItem(key, value)
            return
        
        current = self.buckets[idx]
        while current:
            if current.key == key:
                current.value = value
                return
            if not current.next:
                break
            current = current.next
        current.next = NodeItem(key, value)

    def get(self, key):
        idx = self._hash_function(key)
        current = self.buckets[idx]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return 0
