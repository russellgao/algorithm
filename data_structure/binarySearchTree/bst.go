package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {
	values := []int{17, 5, 35, 2, 11, 29, 38, 9, 16, 7}

	// 测试构造二叉树
	node := buildBinarySearchTree(values)

	// 遍历
	traverseBinarySearchTree(node)

	// 搜索
	ok, child := search(node, 11)

	// 删除
	new_node := deleteTreenode(node, 35)

	fmt.Println(new_node)
	fmt.Println(ok, child)
}

// 查找
func search(root *TreeNode, val int) (bool, *TreeNode) {
	if root == nil {
		return false, nil
	}
	if root.Val == val {
		return true, root
	} else if root.Val < val {
		return search(root.Right, val)
	} else {
		return search(root.Left, val)
	}
}

// 插入
func insert(root, node *TreeNode) *TreeNode {
	if root == nil {
		root = node
		return root
	}
	if root.Val > node.Val {
		root.Left = insert(root.Left, node)
	} else {
		root.Right = insert(root.Right, node)
	}
	return root
}

// 删除
func deleteTreenode(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return nil
	}
	if root.Val > val {
		root.Left = deleteTreenode(root.Left, val)
	} else if root.Val < val {
		root.Right = deleteTreenode(root.Right, val)
	} else {
		if root.Left == nil {
			return root.Right
		} else if root.Right == nil {
			return root.Left
		} else {
			min_node := findMinNode(root.Right)
			root.Val = min_node.Val
			root.Right = deleteTreenode(root.Right, min_node.Val)
		}
	}
	return root
}

func findMinNode(root *TreeNode) *TreeNode {
	for root.Left != nil {
		root = root.Left
	}
	return root
}

// 中序遍历
func traverseBinarySearchTree(root *TreeNode) {
	if root == nil {
		return
	}
	traverseBinarySearchTree(root.Left)
	fmt.Println(root.Val)
	traverseBinarySearchTree(root.Right)
}

// 构建二叉搜索树
func buildBinarySearchTree(values []int) *TreeNode {
	var node *TreeNode = nil
	for _, value := range values {
		node = insert(node, &TreeNode{Val: value})
	}
	return node
}
