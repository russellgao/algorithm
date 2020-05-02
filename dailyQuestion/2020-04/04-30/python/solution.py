
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# =============================================
# 方法一
# 递归
#
# =============================================

def reverseBetween1(head, m, n) :
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    # 定义后驱节点
    successor = None

    def reverseN(head, n):
        nonlocal successor
        if n == 1:
            successor = head.next
            return head
        last = reverseN(head.next, n - 1)
        head.next.next = head
        head.next = successor
        return last

    if m == 1:
        return reverseN(head, n)
    head.next = reverseBetween1(head.next, m - 1, n - 1)
    return head


# =============================================
# 方法二
# 迭代
#
# =============================================

def reverseBetween2(head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    if not head :
        return None
    pre, current = None, head
    while m > 1 :
        pre = current
        current = current.next
        n,m = n - 1, m -1
    con, tail = pre,current
    while n :
        tmp = current.next
        current.next = pre
        pre = current
        current = tmp
        n -= 1
    if con:
        con.next = pre
    else :
        head = pre
    tail.next = current
    return head

# 时间复杂度: O(N) 考虑包含 NN 个结点的链表。对每个节点最多会处理
# （第 nn 个结点之后的结点不处理）
# 空间复杂度: O(1)。我们仅仅在原有链表的基础上调整了一些指针，只使用了 O(1)O(1) 的额外存储空间来获得结果。


if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    result = reverseBetween2(node, 2,4)
    print()