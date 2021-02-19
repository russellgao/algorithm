package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isBalanced(root *TreeNode) bool {
	return dfs(root) >= 0
}

func dfs(root *TreeNode) int {
	if root == nil {
		return 0
	}
	leftHigh := dfs(root.Left)
	rightHigh := dfs(root.Right)
	if leftHigh == -1 || rightHigh == -1 || abs(rightHigh-leftHigh) > 1 {
		return -1
	}
	return max(dfs(root.Left), dfs(root.Right)) + 1
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
