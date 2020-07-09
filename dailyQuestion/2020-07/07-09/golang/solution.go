package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	result := &ListNode{Val: 0}
	dummy := result
	tmp := 0
	for l1 != nil || l2 != nil {
		if l1 != nil {
			tmp += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			tmp += l2.Val
			l2 = l2.Next
		}
		val := tmp % 10
		result.Next = &ListNode{Val: val}
		result = result.Next
		tmp /= 10
	}
	if tmp != 0 {
		result.Next = &ListNode{Val: tmp}
	}
	return dummy.Next

}

func main() {
	l1 := &ListNode{Val: 7}
	l1.Next = &ListNode{Val: 8}
	l1.Next.Next = &ListNode{Val: 9}

	l2 := &ListNode{Val: 9}
	l2.Next = &ListNode{Val: 8}
	l2.Next.Next = &ListNode{Val: 7}

	result := addTwoNumbers(l1, l2)
	for result != nil {
		fmt.Println(result.Val)
		result = result.Next
	}
}
