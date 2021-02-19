package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {
	node := &ListNode{Val: 3, Next: &ListNode{Val: 2}}
	node.Next.Next = &ListNode{Val: 0}
	node.Next.Next.Next = &ListNode{Val: -4}
	node.Next.Next.Next.Next = node.Next
	result := detectCycle(node)
	fmt.Println(result)

}

func detectCycle(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	prt2 := getInstances(head)
	if prt2 == nil {
		return nil
	}
	prt1 := head
	if prt1 != prt2 {
		prt1 = prt1.Next
		prt2 = prt2.Next
	}
	return prt1
}

func getInstances(head *ListNode) *ListNode {
	slow := head
	fast := head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		if slow == fast {
			return slow
		}
	}
	return nil
}
