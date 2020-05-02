# 方法三
# 最小堆（优先队列）
# 维护k个链表的当前头位置的值在堆队列中


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """

    import heapq
    que = []
    for item in lists :
        if item :
            heapq.heappush(que,(item.val, item))
    head = ListNode(-1)
    current = head
    while que :
        value, node = heapq.heappop(que)
        current.next= node
        current = current.next
        if node.next :
            heapq.heappush(que, (node.next.val, node.next))
    return head.next


# heapq里比较的机制是从元组首位0开始，即遇到相同，就比较元组下一位，比如(1,2), (1,3)，前者比后者小。

# 时间复杂度：考虑优先队列中的元素不超过 k 个，那么插入和删除的时间代价为 O(\log k)O(logk)，这里最多有 knkn 个点，对于每个点都被插入删除各一次，故总的时间代价即渐进时间复杂度为 O(kn×logk)。
# 空间复杂度：这里用了优先队列，优先队列中的元素不超过 k 个，故渐进空间复杂度为 O(k)。

