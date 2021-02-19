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
	result := sumOfLeftLeaves(root)
	fmt.Printf("%+v", result)
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumOfLeftLeaves(root *TreeNode) int {
	result := 0
	if root == nil {
		return result
	}
	if root.Left != nil && root.Left.Left == nil && root.Left.Right == nil {
		result += root.Left.Val
	}
	result += sumOfLeftLeaves(root.Left)
	result += sumOfLeftLeaves(root.Right)
	return result
}
