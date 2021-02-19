package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

// 方法一 : 递归
func reverseKGroup(head *ListNode, k int) *ListNode {
	current := head
	count := 0
	for current != nil && count != k {
		current = current.Next
		count += 1
	}
	if count == k {
		current = reverseKGroup(current, k)
		for count != 0 {
			tmp := head.Next
			head.Next = current
			current = head
			head = tmp
			count -= 1
		}
		head = current
	}
	return head
}

// 方法二 尾插法
func reverseKGroup2(head *ListNode, k int) *ListNode {
	dummy := &ListNode{Val: 0}
	dummy.Next = head
	pre := dummy
	tail := dummy
	for {
		count := k
		for count != 0 && tail != nil {
			count -= 1
			tail = tail.Next
		}
		if tail == nil {
			break
		}
		head = pre.Next
		for pre.Next != tail {
			current := pre.Next
			pre.Next = current.Next
			current.Next = tail.Next
			tail.Next = current
		}
		pre = head
		tail = head
	}
	return dummy.Next
}

// 方法三
// 递归
func reverseKGroup3(head *ListNode, k int) *ListNode {
	if head == nil {
		return nil
	}
	count := 0
	temp := head
	for temp != nil && count < k {
		count += 1
		temp = temp.Next
	}
	if count < k {
		return head
	}
	current := head
	var pre *ListNode = nil
	for current != temp {
		next := current.Next
		current.Next = pre
		pre = current
		current = next
	}
	head.Next = reverseKGroup3(temp, k)
	return pre
}

func main() {
	node := &ListNode{Val: 1, Next: &ListNode{Val: 2}}
	node.Next.Next = &ListNode{Val: 3}
	node.Next.Next.Next = &ListNode{Val: 4}
	node.Next.Next.Next.Next = &ListNode{Val: 5}

	result := reverseKGroup3(node, 3)
	fmt.Println(result)
}
