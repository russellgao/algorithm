# 方法二
# 分治合并
# 考虑优化方法一，用分治的方法进行合并


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

    def merge(lists,left,right) :
        if left == right :
            return lists[left]
        if left > right :
            return None
        mid = (left + right) >> 1
        _left = merge(lists,left,mid)
        _right = merge(lists,mid+1,right)
        return mergeTwo(_left,_right)

    return merge(lists,0,len(lists)-1)

# 时间复杂度： 渐进时间复杂度为 O(kn \times \log k)O(kn×logk)
# 空间复杂度：递归会使用到 O(\log k)O(logk) 空间代价的栈空间。

