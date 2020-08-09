package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}
	if p == nil || q == nil {
		return false
	}
	if p.Val != q.Val {
		return false
	}
	return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}

func main() {
	node1 := &TreeNode{Val: 1}
	node1.Left = &TreeNode{Val: 2}
	node1.Right = &TreeNode{Val: 3}

	node2 := &TreeNode{Val: 1}
	node2.Right = &TreeNode{Val: 2}
	node2.Left = &TreeNode{Val: 3}

	result := isSameTree(node1, node2)
	fmt.Println(result)
}
