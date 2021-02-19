package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {
	root := &TreeNode{Val: 3, Left: &TreeNode{Val: 5}, Right: &TreeNode{Val: 1}}
	root.Left.Left = &TreeNode{Val: 6}
	root.Left.Right = &TreeNode{Val: 2, Left: &TreeNode{Val: 7}, Right: &TreeNode{Val: 4}}
	root.Right.Left = &TreeNode{Val: 0}
	root.Right.Right = &TreeNode{Val: 8}
	result := lowestCommonAncestor2(root, &TreeNode{Val: 5}, &TreeNode{Val: 1})
	fmt.Println(result)
}

// 方法一
// 递归
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	if root.Val == p.Val || root.Val == q.Val {
		return root
	}
	left := lowestCommonAncestor(root.Left, p, q)
	right := lowestCommonAncestor(root.Right, p, q)
	if left != nil && right != nil {
		//p,q 节点公共节点是其他节点
		return root
	}
	// 公共节点是p或者q节点
	if left == nil {
		return right
	}
	return left
}

// 方法二
// 存储父节点
func lowestCommonAncestor2(root, p, q *TreeNode) *TreeNode {
	parent := map[int]*TreeNode{}
	visterd := map[int]bool{}
	var dfs func(root *TreeNode)
	dfs = func(root *TreeNode) {
		if root == nil {
			return
		}
		// 存储父节点，key 为左右子树的Val，key 为 父节点
		if root.Left != nil {
			parent[root.Left.Val] = root
			dfs(root.Left)
		}
		if root.Right != nil {
			parent[root.Right.Val] = root
			dfs(root.Right)
		}
	}
	dfs(root)
	// 遍历从p节点到root的访问路径
	for p != nil {
		visterd[p.Val] = true
		p = parent[p.Val]
	}
	// 从q开始跳到root，如果找到第一个p访问过的节点，即为最小公共父节点
	for q != nil {
		if visterd[q.Val] {
			return q
		}
		q = parent[q.Val]
	}
	return nil
}
