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
	result := preorderTraversal(root)
	fmt.Println(result)

}

// 迭代 前序遍历二叉树
func preorderTraversal(root *TreeNode) []int {
	result := []int{}
	if root == nil {
		return result
	}
	queue := []*TreeNode{root}
	for len(queue) != 0 {
		root = queue[len(queue)- 1]
		queue = queue[:len(queue) - 1]
		if root != nil {
			result = append(result, root.Val)
			if root.Right != nil {
				queue = append(queue, root.Right)
			}
			if root.Left != nil {
				queue = append(queue, root.Left)
			}
		}
	}

	return result
}