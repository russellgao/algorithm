package main

import "fmt"

func longestValidParentheses(s string) int {
	n := len(s)
	result := 0
	if n == 0 {
		return result
	}
	stack := []int{-1}
	for i := 0; i < n; i++ {
		if s[i] == '(' {
			stack = append(stack, i)
		} else {
			stack = stack[:len(stack)-1]
			if len(stack) == 0 {
				stack = append(stack, i)
			} else {
				result = max(result, i-stack[len(stack)-1])
			}
		}
	}
	return result
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	s := "(())()"
	result := longestValidParentheses(s)
	fmt.Println(result)
}
