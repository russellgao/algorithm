class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def partition(head: ListNode, x: int) -> ListNode:
    l1 = ListNode(0)
    l2 = ListNode(0)
    l1_pre = l1
    l2_pre = l2

    while head:
        if head.val < x:
            l1.next = ListNode(head.val)
            l1 = l1.next
        else:
            l2.next = ListNode(head.val)
            l2 = l2.next
        head = head.next
    l1_pre = l1_pre.next
    l2_pre = l2_pre.next
    if not l1_pre:
        return l2_pre
    result = l1_pre
    while l1_pre.next:
        l1_pre = l1_pre.next
    l1_pre.next = l2_pre
    return result


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    x = 3

    result = partition(head, x)
    print(result)
