package main

import (
	"fmt"
	"strings"
)

func main() {
	result := generateParenthesis(4)
	fmt.Println(result)
}

func generateParenthesis(n int) (result []string) {
	var dfs func(S []string, left, right int)
	dfs = func(S []string, left, right int) {
		if len(S) == 2*n {
			result = append(result, strings.Join(S, ""))
			return
		}
		if left < n {
			S = append(S, "(")
			dfs(S, left+1, right)
			S = S[:len(S)-1]
		}
		if right < left {
			S = append(S, ")")
			dfs(S, left, right+1)
			S = S[:len(S)-1]
		}
	}
	dfs([]string{}, 0, 0)
	return
}
