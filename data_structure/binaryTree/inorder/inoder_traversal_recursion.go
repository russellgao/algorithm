package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {

	root := &TreeNode{Val: 1, Left: &TreeNode{Val: 2}, Right: &TreeNode{Val: 2}}
	root.Left.Left = &TreeNode{Val: 3}
	root.Left.Right = &TreeNode{Val: 4}
	root.Right.Left = &TreeNode{Val: 4}
	root.Right.Right = &TreeNode{Val: 3}
	result := inorderTraversal(root)
	fmt.Println(result)

}

// 递归 中序遍历二叉树
func inorderTraversal(root *TreeNode) []int {
	result := []int{}
	if root == nil {
		return result
	}
	left := inorderTraversal(root.Left)
	if len(left) != 0 {
		result = append(result, left...)
	}
	result = append(result, root.Val)
	right := inorderTraversal(root.Right)
	if len(right) != 0 {
		result = append(result, right...)
	}
	return result
}
