package main

import (
	"fmt"
)

func main() {
	s := "00110011"
	result := countBinarySubstrings(s)
	fmt.Println(result)

}
func countBinarySubstrings(s string) int {
	if s == "" {
		return 0
	}
	pre, cur := 0, 0
	count := 1
	result := 0
	for i := 1; i < len(s); i++ {
		if s[i] != s[i-1] {
			pre, cur = cur, count
			result += min(pre, cur)
			count = 1
			continue
		}
		count++
	}
	result += min(cur, count)

	return result
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
