package main

import (
	"fmt"
)

func wordBreak(s string, wordDict []string) bool {
	wordDictSet := make(map[string]bool)
	maxlen := 0
	for _, item := range wordDict {
		wordDictSet[item] = true
		if len(item) > maxlen {
			maxlen = len(item)
		}
	}
	length := len(s)
	dp := make([]bool, length+1)
	dp[0] = true
	for i := 1; i <= length; i++ {
		for j := 0; j < i; j++ {
			if len(s[j:i]) > maxlen {
				continue
			}
			if dp[j] && wordDictSet[s[j:i]] {
				dp[i] = true
				break
			}
		}
	}
	return dp[length]
}

func main() {
	s := "catsand"
	wordDict := []string{"cats", "dog", "sand", "and", "cat"}
	result := wordBreak(s, wordDict)
	fmt.Println(result)
}
