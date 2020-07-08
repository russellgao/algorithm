package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func hasPathSum(root *TreeNode, sum int) bool {
	if root == nil {
		return false
	}
	queue := []*TreeNode{root}
	for len(queue) != 0 {
		root = queue[len(queue)-1]
		queue = queue[:len(queue)-1]
		if root.Left == nil && root.Right == nil {
			if root.Val == sum {
				return true
			}
		} else {
			if root.Left != nil {
				item := root.Left
				item.Val = item.Val + root.Val
				queue = append(queue, item)
			}
			if root.Right != nil {
				item := root.Right
				item.Val += root.Val
				queue = append(queue, item)
			}
		}
	}

	return false
}

func main() {
	node := &TreeNode{Val: 4}
	result := hasPathSum(node,22)
	fmt.Println(result)
}
