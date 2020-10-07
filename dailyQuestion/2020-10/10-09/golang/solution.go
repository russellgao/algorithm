package main

import (
	"fmt"
)

func main() {

	head := &ListNode{Val: 1}
	head.Next = &ListNode{Val: 2}
	head.Next.Next = &ListNode{Val: 3}
	head.Next.Next.Next = &ListNode{Val: 4}
	head.Next.Next.Next.Next = &ListNode{Val: 5}
	result := removeNthFromEnd(head, 2)
	fmt.Println(result)
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	length := 0
	dummy := &ListNode{Val: 0}
	dummy.Next = head
	first := head
	for first != nil {
		length++
		first = first.Next
	}
	length -= n
	first = dummy
	for length > 0 {
		first = first.Next
		length--
	}
	first.Next = first.Next.Next
	return dummy.Next
}
