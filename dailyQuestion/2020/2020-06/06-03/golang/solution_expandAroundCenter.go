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
	for i := 0; i < len(s); i++ {
		result += expandAroundCentor(s, i, i)
		result += expandAroundCentor(s, i, i+1)
	}
	return result
}

func expandAroundCentor(s string, i, j int) int {
	result := 0
	for ; i >= 0 && j < len(s) && s[i] == s[j]; i, j = i-1, j+1 {
		result++
	}
	return result
}
