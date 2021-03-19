import math

class LRUCache:
    """
    Method 1 : Saving values in a dictionary with an added 'clock' value 
    put() is O(n) to find key with the smallest clock value.

    Method 2 : Using an OrderedDict instead of a dictionary. OrderedDict is a combination of  HashMap and a LinkedList. OrderedDict has a function called 'moveToEnd()' by key. O(1)

    Method 3 : Using a DoubleLinkedList to store the key-value and doctionary to store these nodes by key. O(1)
    """

    def __init__(self, capacity):
        self.putCount = 0
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        self.putCount+=1
        if key in self.cache:
            self.cache[key][1] = self.putCount
            return self.cache[key][0]
        return -1
    
    def put(self, key, value):
        self.putCount+=1
        if len(self.cache.keys()) < self.capacity:
            self.cache[key] = [value, self.putCount]
        else:
            # Removing LRU key - O(N)
            minKey, minPutCount = 0, math.inf
            for k, v in self.cache.items():
                if v[1] < minPutCount:
                    minKey = k
                    minPutCount = v[1]
            del self.cache[minKey]
            self.cache[key] = [value, self.putCount]

c = LRUCache(3)
c.put(1, 1)
c.put(2, 2)
c.put(3, 3)
c.get(3)
c.get(2)
c.get(2)
c.put(4, 4)
print(c.cache)
print(c.putCount)
