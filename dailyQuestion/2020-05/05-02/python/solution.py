# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 方法一
# 先用快慢指针把链表一分为二，然后反转后面一部分， 再把两个链表拼接在一起

def reorderList(head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head or not head.next or not head.next.next:
        return
    slow = head
    fast = head
    while fast.next and fast.next.next :
        slow = slow.next
        fast = fast.next.next
    newhead = slow.next
    slow.next = None
    def reverse(head) :
        pre = None
        current = head
        while current :
            tmp = current.next
            current.next = pre
            pre = current
            current = tmp
        return pre
    newhead = reverse(newhead)

    while newhead :
        newhead_next = newhead.next
        newhead.next = head.next
        head.next = newhead
        head = newhead.next
        newhead = newhead_next

# 方法二 递归法
def reorderList_recursion(head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

    def reorderListHelp(head, n):
        if n == 1:
            outtail = head.next
            head.next = None
            return outtail
        if n == 2:
            outtail = head.next.next
            head.next.next = None
            return outtail
        tail = reorderListHelp(head.next, n - 2)
        subhead = head.next
        head.next = tail
        outtail = tail.next
        tail.next = subhead
        return outtail

    if not head or not head.next or not head.next.next:
        return
    count = 0
    current = head
    while current:
        current = current.next
        count += 1
    reorderListHelp(head, count)


if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    reorderList_recursion(node)
    print()
