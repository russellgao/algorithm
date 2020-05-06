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
	node := &TreeNode{Val: 1, Left: &TreeNode{Val: 4}, Right: &TreeNode{Val: 3}}
	node.Left.Left = &TreeNode{Val: 2}
	node.Left.Right = &TreeNode{Val: 4}

	node.Right.Left = &TreeNode{Val: 2}
	node.Right.Right = &TreeNode{Val: 5}

	node.Right.Right.Left = &TreeNode{Val: 4}
	node.Right.Right.Right = &TreeNode{Val: 6}

	sum := maxSumBST(node)
	fmt.Println(sum)
}

// 后续遍历
// 左右节点为root时 若均符合， 如果该节点与左右节点值也符合， 那么继续向上层返回true, 以及sum
// 注意 子节点为nil，以及不符合要求的情况
func maxSumBST(root *TreeNode) int {
	result := 0
	helper(root, &result)

	return result
}

func helper(root *TreeNode, result *int) (bool, int) {
	if root == nil {
		return true, 0
	}
	var (
		ok1, ok2   bool
		val1, val2 int
	)

	if root.Left == nil {
		ok1 = true
	} else {
		ok1, val1 = helper(root.Left, result)
	}

	if root.Right == nil {
		ok2 = true
	} else {
		ok2, val2 = helper(root.Right, result)
	}

	if ok1 && ok2 &&
		(root.Left == nil || (root.Left != nil && root.Left.Val < root.Val)) &&
		((root.Right == nil) || (root.Right != nil && root.Right.Val > root.Val)) {

		*result = max(*result, root.Val+val1+val2)

		return true, root.Val + val1 + val2
	}

	return false, 0
}

func max(i, j int) int {
	if i > j {
		return i
	}
	return j
}
