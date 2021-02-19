package main

import (
	"fmt"
)

func main() {

	root := &TreeNode{Val: 4, Left: &TreeNode{Val: 1}, Right: &TreeNode{Val: 6}}
	root.Left.Left = &TreeNode{Val: 0}
	root.Left.Right = &TreeNode{Val: 2, Right: &TreeNode{Val: 3}}
	root.Right.Left = &TreeNode{Val: 5}
	root.Right.Right = &TreeNode{Val: 7, Right: &TreeNode{Val: 8}}

	node2 := &TreeNode{Val: 4, Left: &TreeNode{Val: 1}, Right: &TreeNode{Val: 6}}
	node2.Left.Left = &TreeNode{Val: 0}
	node2.Left.Right = &TreeNode{Val: 2, Right: &TreeNode{Val: 3}}
	node2.Right.Left = &TreeNode{Val: 5}
	node2.Right.Right = &TreeNode{Val: 7, Right: &TreeNode{Val: 8}}
	result := mergeTrees(root, node2)
	fmt.Println(result)
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func mergeTrees(t1 *TreeNode, t2 *TreeNode) *TreeNode {
	if t1 == nil && t2 == nil {
		return nil
	}
	if t1 == nil {
		return t2
	}
	if t2 == nil {
		return t1
	}
	t1.Val = t1.Val + t2.Val
	t1.Left = mergeTrees(t1.Left, t2.Left)
	t1.Right = mergeTrees(t1.Right, t2.Right)
	return t1
}
