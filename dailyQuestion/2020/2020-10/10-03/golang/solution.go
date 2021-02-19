package main

import (
	"fmt"
)

func main() {
	root := &TreeNode{Val: 5, Left: &TreeNode{Val: 4}, Right: &TreeNode{Val: 6}}
	root.Left.Left = &TreeNode{Val: 2}
	root.Left.Right = &TreeNode{Val: 4}
	root.Left.Left = &TreeNode{Val: 1}
	result := kthLargest(root, 3)
	fmt.Println(result)
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthLargest(root *TreeNode, k int) int {
	count := 1
	queue := []*TreeNode{}
	for root != nil || len(queue) > 0 {
		for root != nil {
			queue = append(queue, root)
			root = root.Right
		}
		root = queue[len(queue)-1]
		queue = queue[:len(queue)-1]
		if count == k {
			return root.Val
		}
		count++
		root = root.Left
	}
	return -1
}
