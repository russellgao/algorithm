

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 迭代
def sortList(head: ListNode) -> ListNode:
    head_len = 0
    invc = 1
    h = head
    while h :
        head_len += 1
        h = h.next
    result = ListNode(0)
    result.next = head
    while invc <= head_len :
        pre = result
        h = result.next
        while h :
            h1 ,i = h , invc
            while i and h :
                i -= 1
                h = h.next
            if i :
                break
            h2, i = h, invc
            while i and h :
                i -= 1
                h = h.next
            c1, c2 = invc, invc-i
            while c1 and c2 :
                if h1.val > h2.val :
                    pre.next = h2
                    h2 = h2.next
                    c2 -= 1
                else :
                    pre.next = h1
                    h1 = h1.next
                    c1 -= 1
                pre = pre.next
            pre.next = h1 if c1 else h2
            while c1 > 0 or c2 > 0 :
                pre = pre.next
                c1 -= 1
                c2 -= 1
            pre.next = h
        invc <<= 1
    return result.next


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

