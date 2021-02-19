

package main

import (
	"fmt"
	"strconv"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

var paths []string

func binaryTreePaths(root *TreeNode) []string {
	paths = []string{}
	if root == nil {
		return []string{}
	}
	recurse(root, "")
	return paths
}

func recurse(root *TreeNode, path string) {
	if root != nil {
		path = path + strconv.Itoa(root.Val)
		if root.Left == nil && root.Right == nil {
			paths = append(paths, path)
		} else {
			path += "->"
			recurse(root.Left, path)
			recurse(root.Right, path)
		}
	}
}

func main() {
	root := &TreeNode{Val: 1}
	fmt.Println(binaryTreePaths(root))
}
