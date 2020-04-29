class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 方法一
# 递归，原问题可以拆分成自问题，并且自问题和原问题的问题域完全一样
# 本题以前k个listnode 为原子进行递归

def reverseKGroup1(head: ListNode, k: int) -> ListNode:
    cur = head
    count = 0
    while cur and count!= k:
        cur = cur.next
        count += 1
    if count == k:
        # 以k个进行递归
        cur = reverseKGroup(cur, k)
        while count:
            # 在k个单位内进行反转
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp
            count -= 1
        head = cur
    return head


# 方法二
def reverseKGroup2(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    tail = dummy
    while True:
        count = k
        while count and tail:
            count -= 1
            tail = tail.next
        if not tail:
            break
        head = pre.next
        while pre.next != tail:
            cur = pre.next  # 获取下一个元素
            # pre与cur.next连接起来,此时cur(孤单)掉了出来
            pre.next = cur.next
            cur.next = tail.next  # 和剩余的链表连接起来
            tail.next = cur  # 插在tail后面
        # 改变 pre tail 的值
        pre = head
        tail = head
    return dummy.next


if __name__ == "__main__" :
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    result = reverseKGroup2(node,2)
    print()
