# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode(0)
    dummy = result
    tmp = 0
    while l1 or l2 :
        if l1 :
            tmp += l1.val
            l1 = l1.next
        if l2 :
            tmp += l2.val
            l2 = l2.next
        val = tmp % 10
        result.next = ListNode(val)
        result = result.next
        tmp = tmp // 10
    if tmp != 0 :
        result.next = ListNode(tmp)
    return dummy.next

if __name__ == "__main__" :
    l1 = ListNode(7)
    l1.next = ListNode(8)
    l1.next.next = ListNode(9)

    l2 = ListNode(9)
    l2.next = ListNode(8)
    l2.next.next = ListNode(7)
    result = addTwoNumbers(l1,l2)
    while result :
        print(result.val)
        result = result.next

