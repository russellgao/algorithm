

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 递归
def sortList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    mid, slow.next = slow.next, None
    left, right = sortList(head), sortList(mid)
    h = result = ListNode(0)
    while left and right:
        if left.val > right.val:
            h.next = right
            right = right.next
        else:
            h.next = left
            left = left.next
        h = h.next
    h.next = left if left else right
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

