# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    tmp = 0
    result = ListNode(0)
    dummy = result
    while l1 or l2:
        v = tmp
        if l1:
            v += l1.val
            l1 = l1.next
        if l2:
            v += l2.val
            l2 = l2.next
        result.next = ListNode(v % 10)
        tmp = v // 10
        result = result.next
    if tmp != 0:
        result.next = ListNode(tmp)
    return dummy.next

if __name__ == "__main__" :
    node1 = ListNode(7)
    node1.next = ListNode(1)
    node1.next.next = ListNode(6)
    node2 = ListNode(5)
    node2.next = ListNode(9)
    node2.next.next = ListNode(8)
    node2.next.next.next = ListNode(7)
    node2.next.next.next.next = ListNode(6)

    result = addTwoNumbers(node1, node2)
    while result :
        print(result.val)
        result = result.next
