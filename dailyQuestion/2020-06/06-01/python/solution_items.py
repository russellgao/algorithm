

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 迭代
def sortList(head: ListNode) -> ListNode:
    h, length, intv = head, 0, 1
    while h:
        h, length = h.next, length + 1
    res = ListNode(0)
    res.next = head
    # merge the list in different intv.
    while intv < length:
        pre, h = res, res.next
        while h:
            # get the two merge head `h1`, `h2`
            h1, i = h, intv
            while i and h:
                h, i = h.next, i - 1
            if i:
                break  # no need to merge because the `h2` is None.
            h2, i = h, intv
            while i and h:
                h, i = h.next, i - 1
            c1, c2 = intv, intv - i  # the `c2`: length of `h2` can be small than the `intv`.
            # merge the `h1` and `h2`.
            while c1 and c2:
                if h1.val < h2.val:
                    pre.next = h1
                    h1 = h1.next
                    c1 = c1 - 1
                else:
                    pre.next = h2
                    h2 = h2.next
                    c2 = c2 -1
                pre = pre.next
            pre.next = h1 if c1 else h2
            while c1 > 0 or c2 > 0:
                pre, c1, c2 = pre.next, c1 - 1, c2 - 1
            pre.next = h
        intv = intv << 1
    return res.next


if __name__ == "__main__" :
    node = ListNode(4)
    node.next = ListNode(2)
    node.next.next = ListNode(1)
    node.next.next.next = ListNode(3)
    node.next.next.next.next = ListNode(5)
    result = sortList(node)
    while result :
        print(result.val)
        result = result.next
    print()

