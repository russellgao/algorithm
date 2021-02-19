package main

import (
	"fmt"
)

func main() {
	s := "10101"
	result := countBinarySubstrings(s)
	fmt.Println(result)

}
func countBinarySubstrings(s string) int {
	if s == "" {
		return 0
	}
	counts := []int{}
	count := 1
	for i := 1; i < len(s); i++ {
		if s[i] != s[i-1] {
			counts = append(counts, count)
			count = 1
			continue
		}
		count++
	}
	counts = append(counts, count)
	if len(counts) < 2 {
		return 0
	}
	result := 0
	for i := 1; i < len(counts); i++ {
		result += min(counts[i], counts[i-1])
	}

	return result
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
