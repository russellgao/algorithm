package main

import (
	"fmt"
)

func main() {

	s := "abcabcbb"
	result := lengthOfLongestSubstring(s)
	fmt.Println(result)

}

func lengthOfLongestSubstring(s string) int {
	tmp := map[byte]int{}
	j := 0
	result := 0
	n := len(s)
	for i := 0; i < n; i++ {
		if i != 0 {
			delete(tmp, s[i-1])
		}
		for j < n && tmp[s[j]] == 0 {
			tmp[s[j]]++
			j += 1
		}
		result = max(result, j-i)
	}
	return result
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
