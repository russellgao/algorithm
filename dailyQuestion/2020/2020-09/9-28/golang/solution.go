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
	result := lowestCommonAncestor(root, &TreeNode{Val: 5}, &TreeNode{Val: 1})
	fmt.Println(result)
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	result := root
	for {
		if p.Val < result.Val && q.Val < result.Val {
			result = result.Left
		} else if p.Val > result.Val && q.Val > result.Val {
			result = result.Right
		} else {
			return result
		}
	}
}
