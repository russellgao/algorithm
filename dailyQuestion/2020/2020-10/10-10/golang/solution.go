package main

import (
	"fmt"
)

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

type ListNode struct {
	Val  int
	Next *ListNode
}

func partition(head *ListNode, x int) *ListNode {
	_first := &ListNode{Val: 0}
	_second := &ListNode{Val: 0}
	first_head, first := _first, _first
	second_head, second := _second, _second

	for head != nil {
		if head.Val < x {
			first.Next = head
			first = first.Next
		} else {
			second.Next = head
			second = second.Next
		}
		head = head.Next
	}
	second.Next = nil
	first.Next = second_head.Next
	return first_head.Next
}
