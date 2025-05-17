import collections 

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)

obj = LRUCache(2)
print(obj.get(2))
print(obj.cache)
obj.put(1, 1)
print(obj.cache)
obj.put(2, 2)
print(obj.cache)
print(obj.get(1))
print(obj.cache)