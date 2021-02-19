package main

import "fmt"

func main() {
	root := &TreeNode{Val: 3}
	root.Left = &TreeNode{Val: 1}
	root.Right = &TreeNode{Val: 4}
	root.Right.Left = &TreeNode{Val: 2}

	recoverTree(root)
	fmt.Printf("%+v", root)

}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recoverTree(root *TreeNode) {
	stack := []*TreeNode{}
	var x, y, pre *TreeNode
	for len(stack) > 0 || root != nil {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if pre != nil && root.Val < pre.Val {
			y = root
			if x == nil {
				x = pre
			} else {
				break
			}
		}
		pre = root
		root = root.Right
	}
	x.Val, y.Val = y.Val, x.Val
}
