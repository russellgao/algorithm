
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def listnodeJoin(list1 : ListNode, list2: ListNode) -> ListNode :
    """
    递归调用把两个连接进行拼接，
    :param list1:
    :param list2:
    :return:
    """
    if not list1 :
        return list2
    elif not list2 :
        return list1
    if list1 and not list1.next :
        list1.next = list2
        return list1
    result = listnodeJoin(list1.next, list2)
    list1.next = result
    return list1

def listnodeJoin_items(list1: ListNode, list2: ListNode) -> ListNode :
    """
    当然迭代更容易理解
    :param list1:
    :param list2:
    :return:
    """
    if not list1 :
        return list2
    head = list1
    while list1 and list1.next :
        list1 = list1.next
    list1.next = list2
    return head


if __name__ == "__main__" :
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)

    node2 = ListNode(4)
    node2.next = ListNode(5)
    a = listnodeJoin_items(node1, node2)
    print()