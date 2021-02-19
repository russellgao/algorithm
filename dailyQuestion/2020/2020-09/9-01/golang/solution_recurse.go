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

func pathSum(root *TreeNode, sum int) (result [][]int) {
	temp := []int{}
	var dfs func(root *TreeNode, left int)
	dfs = func(root *TreeNode, left int) {
		if root == nil {
			return
		}
		left -= root.Val
		temp = append(temp, root.Val)
		defer func() {
			temp = temp[:len(temp)-1]
		}()
		if root.Left == nil && root.Right == nil && left == 0 {
			result = append(result, append([]int(nil), temp...))
			return
		}
		dfs(root.Left, left)
		dfs(root.Right, left)
	}
	dfs(root, sum)
	return
}
