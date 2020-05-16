package main

type ListNode struct {
   Val int
   Next *ListNode
}
// 方法一 : 递归
func reverseKGroup(head *ListNode, k int) *ListNode {
    current := head
    count := 0
    for current != nil && count != k {
        current = current.Next
        count += 1
    }
    if count == k {
        current = reverseKGroup(current, k)
        for count != 0 {
            tmp := head.Next
            head.Next = current
            current = head
            head = tmp
            count -= 1
        }
        head = current
    }
    return head
}

// 方法二 尾插法
func reverseKGroup2(head *ListNode, k int) *ListNode {
    dummy := &ListNode{Val:0}
    dummy.Next = head
    pre := dummy
    tail := dummy
    for {
        count := k
        for count != 0 && tail != nil {
            count -= 1
            tail = tail.Next
        }
        if tail == nil {
            break
        }
        head = pre.Next
        for pre.Next != tail {
            current := pre.Next
            pre.Next = current.Next
            current.Next = tail.Next
            tail.Next = current
        }
        pre = head
        tail = head
    }
    return dummy.Next
}