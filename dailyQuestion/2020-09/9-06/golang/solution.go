package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {
	root := &TreeNode{Val: 3, Left: &TreeNode{Val: 5}, Right: &TreeNode{Val: 1}}
	root.Left.Left = &TreeNode{Val: 6}
	root.Left.Right = &TreeNode{Val: 2, Left: &TreeNode{Val: 7}, Right: &TreeNode{Val: 4}}
	root.Right.Left = &TreeNode{Val: 0}
	root.Right.Right = &TreeNode{Val: 8}
	result := levelOrderBottom(root)
	fmt.Println(result)
}

func levelOrderBottom(root *TreeNode) [][]int {
	result := [][]int{}
	if root == nil {
		return result
	}
	stack := []*TreeNode{root}
	for len(stack) != 0 {
		level := []int{}
		size := len(stack)
		for i := 0; i < size; i++ {
			node := stack[0]
			stack = stack[1:]
			level = append(level, node.Val)
			if node.Left != nil {
				stack = append(stack, node.Left)
			}
			if node.Right != nil {
				stack = append(stack, node.Right)
			}
		}
		result = append(result, level)
	}
	i, j := 0, len(result)-1
	for i <= j {
		result[i], result[j] = result[j], result[i]
		i++
		j--
	}
	return result
}
