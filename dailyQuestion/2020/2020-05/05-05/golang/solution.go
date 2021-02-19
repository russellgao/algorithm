package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 方法一
// 中序遍历
func isValidBST(root *TreeNode) bool {
	stack := []*TreeNode{}
	inorder := math.MinInt64
	for len(stack) != 0 || root != nil {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if root.Val <= inorder {
			return false
		}
		inorder = root.Val
		root = root.Right
	}
	return true
}


// 方法二
//递归
func isValidBST2(root *TreeNode) bool {
	return helper(root,math.MinInt64,math.MaxInt64)
}

func helper(root *TreeNode, lower, upper int) bool {
	if root == nil {
		return true
	}
	if root.Val <= lower || root.Val >= upper {
		return false
	}
	return helper(root.Left,lower,root.Val) && helper(root.Right, root.Val, upper)
}

func main() {
	a := &TreeNode{Val: 2}
	a.Left = &TreeNode{Val: 1}
	a.Right = &TreeNode{Val: 3}
	b := isValidBST(a)
	fmt.Println(b)
}