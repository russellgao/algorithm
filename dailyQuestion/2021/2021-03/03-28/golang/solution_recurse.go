package main

import (
	"fmt"
)

func main() {
	root := &TreeNode{
		Val:   7,
		Left:  &TreeNode{Val: 3},
		Right: &TreeNode{Val: 15, Left: &TreeNode{Val: 9}, Right: &TreeNode{Val: 20}},
	}
	obj := Constructor(root)
	param_1 := obj.Next()
	param_2 := obj.Next()
	param_3 := obj.HasNext()
	param_4 := obj.Next()
	param_5 := obj.HasNext()
	param_6 := obj.Next()
	param_7 := obj.HasNext()
	param_8 := obj.Next()
	param_9 := obj.HasNext()

	fmt.Println(param_1)
	fmt.Println(param_2)
	fmt.Println(param_3)
	fmt.Println(param_4)
	fmt.Println(param_5)
	fmt.Println(param_6)
	fmt.Println(param_7)
	fmt.Println(param_8)
	fmt.Println(param_9)

}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type BSTIterator struct {
	l []int
}

func Constructor(root *TreeNode) BSTIterator {
	l := getVals(root)
	return BSTIterator{l: l}
}

func (this *BSTIterator) Next() int {
	x := this.l[0]
	this.l = this.l[1:len(this.l)]
	return x
}

func (this *BSTIterator) HasNext() bool {
	return len(this.l) > 0
}

func getVals(root *TreeNode) []int {
	res := []int{}
	if root == nil {
		return res
	}
	res = append(res, getVals(root.Left)...)
	res = append(res, root.Val)
	res = append(res, getVals(root.Right)...)
	return res
}
