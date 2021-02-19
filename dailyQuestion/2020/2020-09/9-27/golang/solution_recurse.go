package main

import (
	"fmt"
)

func main() {
	result := buildTree([]int{9, 3, 15, 20, 7}, []int{9, 15, 7, 20, 3})
	fmt.Println(result)
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(inorder []int, postorder []int) *TreeNode {
	if len(inorder) == 0 {
		return nil
	}
	node := &TreeNode{Val: postorder[len(postorder)-1]}
	_inorder := []int{}
	for _, v := range inorder {
		if v == postorder[len(postorder)-1] {
			break
		}
		_inorder = append(_inorder, v)
	}
	inorder_n := len(_inorder)
	node.Left = buildTree(_inorder, postorder[:inorder_n])
	node.Right = buildTree(inorder[inorder_n+1:], postorder[inorder_n:len(postorder)-1])
	return node
}
