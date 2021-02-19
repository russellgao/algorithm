package main

import "fmt"

// Definition for singly-linked list.
type ListNode struct {
    Val int
    Next *ListNode
}

// 方法一
// 先用快慢指针把链表一分为二，然后反转后面一部分， 再把两个链表拼接在一起
func reorderList(head *ListNode)  {
    if head == nil || head.Next == nil || head.Next.Next == nil {
        return
    }
    slow := head
    fast := head
    for fast.Next != nil && fast.Next.Next != nil{
        slow = slow.Next
        fast = fast.Next.Next
    }
    newhead := slow.Next
    slow.Next = nil
    newhead = reverse(newhead)
    for newhead != nil {
        tmp := newhead.Next
        newhead.Next = head.Next
        head.Next = newhead
        head = newhead.Next
        newhead = tmp
    }
}

func reverse(head *ListNode) *ListNode {
    var pre *ListNode = nil
    current := head
    for current != nil {
        current_next := current.Next
        current.Next = pre
        pre = current
        current = current_next
    }
    return pre
}

// 方法二
// 递归



func reorderList_recursion(head *ListNode) {
	if head == nil || head.Next == nil || head.Next.Next == nil {
		return
	}
	count := 0
	current := head
	for current != nil {
		count += 1
		current = current.Next
	}
	reorderListHelp(head, count)

}

func reorderListHelp(head *ListNode, n int) *ListNode {
	if n == 1 {
		outtail := head.Next
		head.Next = nil
		return outtail
	}
	if n == 2 {
		outtail := head.Next.Next
		head.Next.Next = nil
		return outtail
	}
	tail := reorderListHelp(head.Next, n-2)
	tmp := head.Next
	head.Next = tail
	outtail := tail.Next
	tail.Next = tmp
	return outtail
}

func main() {
	a := &ListNode{Val: 1}
	a.Next = &ListNode{Val: 2}
	a.Next.Next = &ListNode{Val: 3}
	a.Next.Next.Next = &ListNode{Val: 4}
	a.Next.Next.Next.Next = &ListNode{Val: 5}
	reorderList_recursion(a)
	currrent := a
	for currrent != nil {
		fmt.Println(currrent.Val)
		currrent = currrent.Next
	}

}