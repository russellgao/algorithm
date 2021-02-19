package main

// Definition for singly-linked list.
type ListNode struct {
    Val int
    Next *ListNode
}


// 用递归反转链表
func reverseList(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }
    if head.Next == nil {
        return head
    }
    last := reverseList(head.Next)
    head.Next.Next = head
    head.Next = nil
    return last
}

// 用迭代的方式反转链表
func reverseList_items(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }
    // 初始化一个空节点
    var pre *ListNode = nil
    current := head
    for current != nil {
        tmp := current.Next
        current.Next = pre
        pre = current
        current = tmp
    }
    return pre
}