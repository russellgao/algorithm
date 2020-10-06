package main

import (
	"fmt"
	"math"
)

func main() {
	root := &TreeNode{Val: 3, Left: &TreeNode{Val: 5}, Right: &TreeNode{Val: 1}}
	root.Left.Left = &TreeNode{Val: 6}
	root.Left.Right = &TreeNode{Val: 2}
	root.Right.Left = &TreeNode{Val: 0}
	result := countNodes(root)
	fmt.Println(result)
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func countNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}
	d := compute_depth(root)
	if d == 0 {
		return 1
	}
	left, right := 1, int(math.Pow(2, float64(d)))-1
	for left <= right {
		mid := left + (right-left)/2
		if exists(mid, d, root) {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return (int(math.Pow(2, float64(d))) - 1) + left
}

func compute_depth(root *TreeNode) int {
	d := 0
	for root.Left != nil {
		root = root.Left
		d++
	}
	return d
}

func exists(idx, d int, node *TreeNode) bool {
	left, right := 0, int(math.Pow(2, float64(d)))-1
	for i := 0; i < d; i++ {
		mid := left + (right-left)/2
		if idx <= mid {
			node = node.Left
			right = mid
		} else {
			node = node.Right
			left = mid + 1
		}
	}
	return node != nil
}
