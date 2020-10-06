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
	result := increasingBST(root)
	fmt.Println(result)
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func increasingBST(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	node := &TreeNode{Val: 0}
	result := node
	queue := []*TreeNode{}
	for root != nil || len(queue) > 0 {
		for root != nil {
			queue = append(queue, root)
			root = root.Left
		}
		root = queue[len(queue)-1]
		queue = queue[:len(queue)-1]
		node.Right = &TreeNode{Val: root.Val}
		node = node.Right
		root = root.Right
	}
	return result.Right
}


