package main

import (
	"fmt"
)

func main() {

	s := "abcabcbb"
	result := countSubstrings(s)
	fmt.Println(result)

}

func countSubstrings(s string) int {
	result := 0
	if s == "" {
		return result
	}
	len_s := len(s)
	dp := make([][]int, len_s)
	for i := 0; i < len_s; i++ {
		dp[i] = make([]int, len_s)
	}
	for length := 0; length < len_s; length++ {
		for i := 0; i < len_s-length; i++ {
			j := i + length
			if length == 0 {
				dp[i][j] = 1
			} else if length == 1 {
				if s[i] == s[j] {
					dp[i][j] = 1
				}
			} else {
				if s[i] == s[j] {
					dp[i][j] = dp[i+1][j-1]
				}
			}
			if dp[i][j] == 1 {
				result += 1
			}
		}
	}
	return result
}
