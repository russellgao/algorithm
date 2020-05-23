# 有序字典，把有序字典当作一个属性

from collections import OrderedDict
class LRUCache():

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mappings = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.mappings :
            return -1
        self.mappings.move_to_end(key)
        return self.mappings[key]

    def put(self, key: int, value: int) -> None:
        if key in self.mappings :
            self.mappings.move_to_end(key)
        self.mappings[key] = value
        if len(self.mappings) > self.capacity :
            self.mappings.popitem(last = False)


if __name__ == "__main__" :
    lru = LRUCache(2)
    lru.put(1,1)
    lru.put(2,2)
    a = lru.get(1)
    lru.put(3,3)
    b = lru.get(2)
    lru.put(4,4)
    c = lru.get(1)
    d = lru.get(3)
    e = lru.get(4)

    print()

