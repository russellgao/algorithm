package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func flatten(root *TreeNode) {
	list := preorder(root)
	for i := 1; i < len(list); i++ {
		pre, cur := list[i-1], list[i]
		pre.Left = nil
		pre.Right = cur
	}
}

func preorder(root *TreeNode) []*TreeNode {
	result := []*TreeNode{}
	if root == nil {
		return nil
	}
	result = append(result, root)
	result = append(result, preorder(root.Left)...)
	result = append(result, preorder(root.Right)...)
	return result
}
func main() {
	root := &TreeNode{Val: 1, Left: &TreeNode{Val: 2}, Right: &TreeNode{Val: 5}}
	root.Left.Left = &TreeNode{Val: 3}
	root.Left.Right = &TreeNode{Val: 4}
	root.Right.Right = &TreeNode{Val: 6}
	flatten(root)
}
