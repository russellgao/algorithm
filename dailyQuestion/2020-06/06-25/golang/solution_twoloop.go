package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

// 删除重复的节点
func removeDuplicateNodes(head *ListNode) *ListNode {
	prve1 := head
	for prve1 != nil {
		prev1_1 := prve1
		for prev1_1.Next != nil {
			cur := prev1_1.Next
			if cur.Val == prve1.Val {
				prev1_1.Next = prev1_1.Next.Next
			} else {
				prev1_1 = prev1_1.Next
			}
		}
		prve1 = prve1.Next
	}
	return head
}

func main() {
	head := &ListNode{Val: 1}
	head.Next = &ListNode{Val: 2}
	head.Next.Next = &ListNode{Val: 3}
	head.Next.Next.Next = &ListNode{Val: 3}
	head.Next.Next.Next.Next = &ListNode{Val: 2}
	head.Next.Next.Next.Next.Next = &ListNode{Val: 1}

	result := removeDuplicateNodes(head)
	fmt.Println(result)
}
