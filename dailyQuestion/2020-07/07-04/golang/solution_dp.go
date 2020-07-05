package main

import "fmt"

func longestValidParentheses(s string) int {
	n := len(s)
	result := 0
	if n == 0 {
		return result
	}
	dp := make([]int, len(s))
	for i := 1; i < n; i++ {
		if s[i] == ')' {
			if s[i-1] == '(' {
				if i >= 2 {
					dp[i] = dp[i-2] + 2
				} else {
					dp[i] = 2
				}
			} else if i-dp[i-1] > 0 && s[i-dp[i-1]-1] == '(' {
				if i-dp[i-1] >= 2 {
					dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
				} else {
					dp[i] = dp[i-1] + 2
				}
			}
			result = max(result, dp[i])
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
