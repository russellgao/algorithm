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
	nums := []int{}
	var inorder func(root *TreeNode)
	inorder = func(root *TreeNode) {
		if root == nil {
			return
		}
		inorder(root.Left)
		nums = append(nums, root.Val)
		inorder(root.Right)
	}
	inorder(root)
	x, y := findNum(nums)
	revover(root, 2, x, y)

}

func findNum(nums []int) (int, int) {
	x, y := -1, -1
	for i := 0; i < len(nums)-1; i++ {
		if nums[i+1] < nums[i] {
			y = nums[i+1]
			if x == -1 {
				x = nums[i]
			} else {
				break
			}
		}
	}
	return x, y
}

func revover(root *TreeNode, count, x, y int) {
	if root == nil || count == 0 {
		return
	}
	if root.Val == x || root.Val == y {
		if root.Val == x {
			root.Val = y
		} else {
			root.Val = x
		}
		count--
	}
	revover(root.Left, count, x, y)
	revover(root.Right, count, x, y)
}
