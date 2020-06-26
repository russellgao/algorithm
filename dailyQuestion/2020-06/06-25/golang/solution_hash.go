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
	if head == nil {
		return nil
	}
	tmp := map[int]int{head.Val: 0}
	pos := head
	for pos.Next != nil {
		cur := pos.Next
		if _, ok := tmp[cur.Val]; ok {
			pos.Next = pos.Next.Next
		} else {
			tmp[cur.Val] = 0
			pos = pos.Next
		}
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
