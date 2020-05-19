package main

import (
	"fmt"
)

func main() {
	a := "ebcbbececabbacecbbcbe"
	b := validPalindrome(a)
	fmt.Println(b)
}

func validPalindrome(s string) bool {
	i, j := 0, len(s)-1
	flag := true
	for i <= j {
		if s[i] == s[j] {
			i += 1
			j -= 1
		} else {
			flag = validate(s[i:j]) || validate(s[i+1:j+1])
			break
		}
	}
	return flag
}

func validate(s string) bool {
	i, j := 0, len(s)-1
	for i <= j {
		if s[i] != s[j] {
			return false
		}
		i += 1
		j -= 1
	}
	return true
}
