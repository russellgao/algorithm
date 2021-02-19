# 双向链表求解

class DlinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.next = None
        self.prev = None


class LRUCache():
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = DlinkedNode()
        self.tail = DlinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """ 始终放在head的右边 """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """删除一个节点"""
        _prev = node.prev
        _next = node.next

        _prev.next = _next
        _next.prev = _prev

    def _move_to_head(self, node):
        """
        先删除再增加
        :param node:
        :return:
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        删除最后一个节点的前一个
        :return:
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if not node:
            node = DlinkedNode()
            node.key = key
            node.value = value
            self.size += 1
            self.cache[key] = node
            self._add_node(node)

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)


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
