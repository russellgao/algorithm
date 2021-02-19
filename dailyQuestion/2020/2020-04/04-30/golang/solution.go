package main

// Definition for singly-linked list.
type ListNode struct {
    Val int
    Next *ListNode
}

// 方法一
// 递归

// 方法二
// 迭代
func reverseBetween2(head *ListNode, m int, n int) *ListNode {
    if head == nil {
        return nil
    }
    pre := &ListNode{}
    current := head
    for m > 1 {
        pre = current
        current = current.Next
        m , n = m - 1, n - 1
    }
    con, tail := pre, current
    for n > 0 {
        tmp := current.Next
        current.Next = pre
        pre = current
        current = tmp 
        n -= 1
    }
    if con != nil && con.Next != nil {
        con.Next = pre
    } else {
        head = pre
    }
    tail.Next = current
    return head
}