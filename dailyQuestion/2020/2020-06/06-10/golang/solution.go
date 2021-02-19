package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {

	head := &ListNode{Val: 1}
	head.Next = &ListNode{Val: 4}
	head.Next.Next = &ListNode{Val: 3}
	head.Next.Next.Next = &ListNode{Val: 2}
	head.Next.Next.Next.Next = &ListNode{Val: 5}
	head.Next.Next.Next.Next.Next = &ListNode{Val: 2}

	result := partition(head, 3)
	fmt.Println(result)

}

func partition(head *ListNode, x int) *ListNode {
	l1 := &ListNode{Val: 0}
	l2 := &ListNode{Val: 0}
	l1_pre := l1
	l2_pre := l2
	for head != nil {
		if head.Val < x {
			l1.Next = &ListNode{Val: head.Val}
			l1 = l1.Next
		} else {
			l2.Next = &ListNode{Val: head.Val}
			l2 = l2.Next
		}
		head = head.Next
	}
	l1_pre = l1_pre.Next
	l2_pre = l2_pre.Next
	if l1_pre == nil {
		return l2_pre
	}
	result := l1_pre
	for l1_pre.Next != nil {
		l1_pre = l1_pre.Next
	}
	l1_pre.Next = l2_pre
	return result
}
