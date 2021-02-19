package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {
	S := "1-2--3--4-5--6--7"
	result := recoverFromPreorder(S)
	fmt.Println(result)
}

func recoverFromPreorder(S string) *TreeNode {
	if len(S) == 0 {
		return nil
	}
	stack := []*TreeNode{}
	pos := 0
	for pos < len(S) {
		level := 0
		for S[pos] == '-' {
			level++
			pos++
		}
		value := 0
		for pos < len(S) && (S[pos] >= '0' && S[pos] <= '9') {
			value = value*10 + int(S[pos]-'0')
			pos++
		}
		node := &TreeNode{Val: value}
		if level == len(stack) {
			if len(stack) != 0 {
				stack[len(stack)-1].Left = node
			}
		} else {
			stack = stack[:level]
			stack[level-1].Right = node
		}

		stack = append(stack, node)
	}
	return stack[0]
}
