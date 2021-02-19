# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def partition(head: ListNode, x: int) -> ListNode:

    first = first_head = ListNode(0)
    second = second_head = ListNode(0)

    while head:
        if head.val < x:
            first.next = head
            first = first.next
        else:
            second.next = head
            second = second.next
        head = head.next
    second.next = None
    first.next = second_head.next
    return first_head.next

if __name__ == "__main__" :
    node = ListNode(1)
    node.next = ListNode(4)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(2)
    node.next.next.next.next = ListNode(5)
    node.next.next.next.next.next = ListNode(2)
    result = partition(node,3)
    while result :
        print(result.val)
        result = result.next