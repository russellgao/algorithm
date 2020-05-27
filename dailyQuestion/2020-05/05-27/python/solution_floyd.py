class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head: ListNode) -> ListNode:
    def getInstance(head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return slow
        return None

    if not head:
        return None
    prt2 = getInstance(head)
    if not prt2:
        return None

    prt1 = head
    while prt1 != prt2:
        prt1 = prt1.next
        prt2 = prt2.next
    return prt1


if __name__ == "__main__":
    node = ListNode(3)
    node.next = ListNode(2)
    node.next.next = ListNode(0)
    node.next.next.next = ListNode(-4)
    node.next.next.next.next = node.next
    result = detectCycle(node)
    print(result.val)
