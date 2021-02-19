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
	result := isSymmetric(root)
	fmt.Println(result)

}
// 迭代求解
func isSymmetric(root *TreeNode) bool {
	queue := []*TreeNode{root, root}
	for len(queue) != 0 {
		left, right := queue[0], queue[1]
		queue = queue[2:]
		if left == nil && right == nil {
			continue
		}
		if left == nil || right == nil {
			return false
		}
		if left.Val != right.Val {
			return false
		}
		queue = append(queue, left.Left)
		queue = append(queue, right.Right)
		queue = append(queue, left.Right)
		queue = append(queue, right.Left)
	}
	return true
}
