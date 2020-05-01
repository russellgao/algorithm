# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    """
    递归 反转 链表
    :type head: ListNode
    :rtype: ListNode
    """
    if not head :
        return None
    if not head.next :
        return head
    last = reverseList(head.next)
    head.next.next = head
    head.next = None
    return last

def reverseList_items(head) :
    """
    迭代 反转 链表
    :type head: ListNode
    :rtype: ListNode
    """
    pre = None
    current = head
    while current:
        tmp = current.next
        current.next = pre
        pre = current
        current = tmp
    return pre


if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    result = reverseList(node)
    print()