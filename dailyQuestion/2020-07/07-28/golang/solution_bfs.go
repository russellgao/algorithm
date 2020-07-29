package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	queue := []*TreeNode{root}
	height := 0
	for len(queue) != 0 {
		height++
		size := len(queue)
		stack := []*TreeNode{}
		for size != 0 {
			node := queue[size-1]
			if node.Left != nil {
				stack = append(stack, node.Left)
			}
			if node.Right != nil {
				stack = append(stack, node.Right)
			}
			queue = queue[:size-1]
			size--
		}
		queue = append(queue, stack...)
	}
	return height
}

func main() {
	root := &TreeNode{Val: 3, Left: &TreeNode{Val: 5}, Right: &TreeNode{Val: 1}}
	root.Left.Left = &TreeNode{Val: 6}
	root.Left.Right = &TreeNode{Val: 2, Left: &TreeNode{Val: 7}, Right: &TreeNode{Val: 4}}
	root.Right.Left = &TreeNode{Val: 0}
	root.Right.Right = &TreeNode{Val: 8}
	result := maxDepth(root)
	fmt.Println(result)
}
