package main

import (
	"fmt"
)

func main() {
	root := &TreeNode{Val: 3, Left: &TreeNode{Val: 5}, Right: &TreeNode{Val: 1}}
	root.Left.Left = &TreeNode{Val: 6}
	root.Left.Right = &TreeNode{Val: 2, Left: &TreeNode{Val: 7}, Right: &TreeNode{Val: 4}}
	root.Right.Left = &TreeNode{Val: 0}
	root.Right.Right = &TreeNode{Val: 8}
	result := listOfDepth(root)
	fmt.Println(result)
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
type ListNode struct {
	Val  int
	Next *ListNode
}

func listOfDepth(tree *TreeNode) []*ListNode {
	if tree == nil {
		return nil
	}
	result := []*ListNode{}
	queue := []*TreeNode{tree}
	for len(queue) > 0 {
		size := len(queue)
		listnode := &ListNode{Val: 0}
		tmp := listnode
		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]
			tmp.Next = &ListNode{Val: node.Val}
			tmp = tmp.Next
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		result = append(result, listnode.Next)
	}
	return result
}
