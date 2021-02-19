package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isBalanced(root *TreeNode) bool {
	if root == nil {
		return true
	}
	return abs(dfs(root.Left)-dfs(root.Right)) <= 1 && isBalanced(root.Left) && isBalanced(root.Right)
}

func dfs(root *TreeNode) int {
	result := 1
	if root == nil {
		return 0
	}
	result += max(dfs(root.Left), dfs(root.Right))
	return result
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func abs(x int) int {
	if x < 0 {
		return -1 * x
	}
	return x
}

func main() {
	root := &TreeNode{Val: 3}
	root.Right = &TreeNode{Val: 20}
	root.Left = &TreeNode{Val: 9}
	root.Right.Left = &TreeNode{Val: 15}
	root.Right.Right = &TreeNode{Val: 20}
	result := isBalanced(root)
	fmt.Println(result)
}
