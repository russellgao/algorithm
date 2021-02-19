package main

import (
	"fmt"
	"strings"
)

func main() {
	S := "A man, a plan, a canal: Panama"
	result := isPalindrome(S)
	fmt.Println(result)
}

func isPalindrome(s string) bool {
	if len(s) == 0 {
		return true
	}
	i, j := 0, len(s)-1
	for i <= j {
		if !((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z') || (s[i] >= '0' && s[i] <= '9')) {
			i++
			continue
		}
		if !((s[j] >= 'a' && s[j] <= 'z') || (s[j] >= 'A' && s[j] <= 'Z') || (s[j] >= '0' && s[j] <= '9')) {
			j--
			continue
		}
		if strings.ToLower(string(s[i])) != strings.ToLower(string(s[j])) {
			return false
		}
		i++
		j--
	}
	return true
}
