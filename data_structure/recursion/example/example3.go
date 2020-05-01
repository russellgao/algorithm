package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {

	a := &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3}}}
	b := &ListNode{Val: 4, Next: &ListNode{Val: 5, Next: &ListNode{Val: 6}}}
	c := ListnodeJoin(a, b)
	for c != nil {
		fmt.Println(c.Val)
		c = c.Next
	}
}


// 递归拼接
func ListnodeJoin(node1, node2 *ListNode) *ListNode {
	if node1 == nil {
		return node2
	}
	if node1.Next == nil {
		node1.Next = node2
		return node1
	}
	node1.Next = ListnodeJoin(node1.Next, node2)
	return node1
}
