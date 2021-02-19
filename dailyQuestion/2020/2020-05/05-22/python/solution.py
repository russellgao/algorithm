# 有序字典，通过继承的方式

from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self :
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self :
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity :
            self.popitem(last = False)


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

