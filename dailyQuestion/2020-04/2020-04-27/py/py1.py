# 方法一
# 顺序合并

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """

    def mergeTwo(list1, list2) :
        head = ListNode()
        pre_head = head
        current_1 = list1
        current_2 = list2
        while current_1 and current_2 :
            if current_1.val < current_2.val :
                pre_head.next = current_1
                current_1 = current_1.next
            else :
                pre_head.next = current_2
                current_2 = current_2.next
            pre_head = pre_head.next
        if current_1 :
            pre_head.next = current_1
        elif current_2 :
            pre_head.next = current_2
        return head.next

    result = None
    for item in lists :
        result = mergeTwo(result,item)
    return result

# 时间复杂度：O(k^2*n)
# 空间复杂度：没有用到与 kk 和 nn 规模相关的辅助空间，故渐进空间复杂度为 O(1)O(1)。