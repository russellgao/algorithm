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
	tmp := map[*ListNode]string{}
	for head != nil {
		if _, ok := tmp[head]; ok {
			return head
		}
		tmp[head] = ""
		head = head.Next
	}
	return nil
}


