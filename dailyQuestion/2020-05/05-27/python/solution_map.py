class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head: ListNode) -> ListNode:
    tmp = {}
    while head:
        if head in tmp:
            return head
        tmp[head] = ""
        head = head.next
    return None


if __name__ == "__main__":
    node = ListNode(3)
    node.next = ListNode(2)
    node.next.next = ListNode(0)
    node.next.next.next = ListNode(-4)
    node.next.next.next.next = node.next
    result = detectCycle(node)
    print(result.val)
