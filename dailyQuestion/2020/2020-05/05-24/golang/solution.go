package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {
	s := "ADOBECODEBANC"
	t := "ABC"
	result := minWindow(s, t)
	fmt.Println(result)

}

func minWindow(s string, t string) string {
	mappings_t := map[byte]int{}
	mappings_windows := map[byte]int{}
	max_len := math.MaxInt32

	for i := 0; i < len(t); i++ {
		mappings_t[t[i]]++
	}
	result_l, result_r := -1, -1
	check := func() bool {
		for k, v := range mappings_t {
			if mappings_windows[k] < v {
				return false
			}
		}
		return true
	}
	for i, j := 0, 0; j < len(s); j++ {
		if mappings_t[s[j]] > 0 {
			mappings_windows[s[j]]++
		}
		for check() && i <= j {
			if j-i+1 < max_len {
				max_len = j - i + 1
				result_l, result_r = i, j
			}
			if _, ok := mappings_t[s[i]]; ok {
				mappings_windows[s[i]]--
			}
			i++
		}
	}
	if result_r == -1 {
		return ""
	}
	return s[result_l : result_r+1]
}
