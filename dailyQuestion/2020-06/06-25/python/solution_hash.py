# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeDuplicateNodes(head: ListNode) -> ListNode:
    if not head :
        return None
    tmp = [head.val]
    pos = head
    while pos.next:
        cur = pos.next
        if cur.val not in tmp:
            tmp.append(cur.val)
            pos = pos.next
        else:
            pos.next = pos.next.next
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

