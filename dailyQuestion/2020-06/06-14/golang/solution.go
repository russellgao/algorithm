package main

import (
	"fmt"
)

func main() {
	strs := []string{"flower", "flow", "flight"}
	result := longestCommonPrefix(strs)

	fmt.Println(result)

}

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	result := strs[0]
	for i := 1; i < len(strs); i++ {
		result_len := min(len(result), len(strs[i]))
		result = result[:result_len]
		for j := 0; j < result_len; j++ {
			if result[j] != strs[i][j] {
				result = result[:j]
				break
			}
		}
	}

	return result
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

