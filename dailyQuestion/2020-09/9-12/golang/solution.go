package main

import "fmt"

func main() {
	root := &TreeNode{Val: 3, Left: &TreeNode{Val: 5}, Right: &TreeNode{Val: 1}}
	root.Left.Left = &TreeNode{Val: 6}
	root.Left.Right = &TreeNode{Val: 2, Left: &TreeNode{Val: 7}, Right: &TreeNode{Val: 4}}
	root.Right.Left = &TreeNode{Val: 0}
	root.Right.Right = &TreeNode{Val: 8}
	result := averageOfLevels(root)
	fmt.Println(result)
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func averageOfLevels(root *TreeNode) []float64 {
	if root == nil {
		return []float64{}
	}
	result := []float64{}
	stack := []*TreeNode{root}
	for len(stack) != 0 {
		sum := 0
		size := len(stack)
		for i := 0; i < size; i++ {
			node := stack[0]
			stack = stack[1:]
			sum += node.Val
			if node.Left != nil {
				stack = append(stack, node.Left)
			}
			if node.Right != nil {
				stack = append(stack, node.Right)
			}
		}
		result = append(result, float64(sum)/float64(size))
	}
	return result
}
