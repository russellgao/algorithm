# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def removeDuplicateNodes(head: ListNode) -> ListNode:
    tmp = []
    dummy = ListNode(0)
    prev = dummy
    while head:
        if head.val in tmp:
            pass
        else:
            dummy.next = ListNode(head.val)
            tmp.append(head.val)
            dummy = dummy.next
        head = head.next
    return prev.next

if __name__ == "__main__" :
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(2)
    head.next.next.next.next.next = ListNode(1)

    result = removeDuplicateNodes(head)

    print(result)

