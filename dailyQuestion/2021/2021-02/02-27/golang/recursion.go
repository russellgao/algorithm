package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "ababbc"
	res := longestSubstring(s, 2)

	fmt.Println(res)
}

func longestSubstring(s string, k int) (res int) {
	if s == "" {
		return
	}
	cnt := [26]int{}
	for _, ch := range s {
		cnt[ch-'a']++
	}

	var split byte
	for i, c := range cnt {
		if 0 < c && c < k {
			split = byte(i) + 'a'
			break
		}
	}
	if split == 0 {
		return len(s)
	}
	for _, subStr := range strings.Split(s, string(split)) {
		res = max(res, longestSubstring(subStr, k))
	}
	return
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
