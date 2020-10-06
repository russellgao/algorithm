package main

import (
	"fmt"
)

func main() {
	root := &TreeNode{Val: 5, Left: &TreeNode{Val: 4}, Right: &TreeNode{Val: 6}}
	root.Left.Left = &TreeNode{Val: 2}
	root.Left.Right = &TreeNode{Val: 4}
	root.Left.Left = &TreeNode{Val: 1}
	result := zigzagLevelOrder(root)
	fmt.Println(result)
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func zigzagLevelOrder(root *TreeNode) (result [][]int) {
	if root == nil {
		return
	}
	count := 0
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		size := len(queue)
		tmp := []int{}
		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]
			tmp = append(tmp, node.Val)
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		if count%2 == 1 {
			reverse(tmp)
		}
		result = append(result, append([]int{}, tmp...))
		count++
	}
	return
}

func reverse(l []int) {
	for i, j := 0, len(l)-1; i < j; i++ {
		l[i], l[j] = l[j], l[i]
		j--
	}
}
