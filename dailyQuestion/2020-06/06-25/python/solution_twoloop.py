# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeDuplicateNodes(head: ListNode) -> ListNode:
    prev1 = head
    while prev1:
        prev11 = prev1
        while prev11.next:
            cur = prev11.next
            if cur.val == prev1.val:
                prev11.next = prev11.next.next
            else:
                prev11 = prev11.next
        prev1 = prev1.next
    return head

if __name__ == "__main__" :
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(2)
    head.next.next.next.next.next = ListNode(1)

    result = removeDuplicateNodes(head)

    print(result)

