package main

import "fmt"

func main() {
	root := &TreeNode{Val: 3, Left: &TreeNode{Val: 5}, Right: &TreeNode{Val: 1}}
	root.Left.Left = &TreeNode{Val: 6}
	root.Left.Right = &TreeNode{Val: 2, Left: &TreeNode{Val: 7}, Right: &TreeNode{Val: 4}}
	root.Right.Left = &TreeNode{Val: 0}
	root.Right.Right = &TreeNode{Val: 8}

	result := pathSum(root, 12)
	fmt.Println(result)

}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type pair struct {
	node *TreeNode
	left int
}

func pathSum(root *TreeNode, sum int) (result [][]int) {
	if root == nil {
		return
	}
	parent := map[*TreeNode]*TreeNode{}
	var getPath func(node *TreeNode) (path []int)
	getPath = func(node *TreeNode) (path []int) {
		for ; node != nil; node = parent[node] {
			path = append(path, node.Val)
		}
		for i, j := 0, len(path)-1; i < j; i++ {
			path[i], path[j] = path[j], path[i]
			j--
		}
		return
	}
	stack := []pair{pair{node: root, left: sum}}
	for len(stack) != 0 {
		p := stack[0]
		stack = stack[1:]
		node := p.node
		left := p.left
		left -= node.Val
		if node.Left == nil && node.Right == nil {
			if left == 0 {
				result = append(result, getPath(node))
			}
		} else {
			if node.Left != nil {
				parent[node.Left] = node
				stack = append(stack, pair{node: node.Left, left: left})
			}
			if node.Right != nil {
				parent[node.Right] = node
				stack = append(stack, pair{node: node.Right, left: left})
			}
		}
	}
	return
}
