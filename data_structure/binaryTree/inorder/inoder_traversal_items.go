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

// 迭代 中序遍历二叉树
func inorderTraversal(root *TreeNode) []int {
	result := []int{}
	queue := []*TreeNode{}
	for root != nil || len(queue) != 0 {
		for root != nil {
			queue = append(queue, root)
			root = root.Left
		}
		root = queue[len(queue)-1]
		queue = queue[:len(queue)-1]
		result = append(result, root.Val)
		root = root.Right
	}
	return result
}
