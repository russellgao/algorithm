package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "Let's take LeetCode contest"
	result := reverseWords(s)
	fmt.Println(result)

}

func reverseWords(s string) string {
	result := ""
	words := strings.Split(s, " ")
	for i, word := range words {
		result += reverseWord(word)
		if i != len(words)-1 {
			result += " "
		}
	}
	return result
}

func reverseWord(s string) string {
	_s := []byte(s)
	i, j := 0, len(s)-1
	for i <= j {
		_s[i], _s[j] = _s[j], _s[i]
		i++
		j--
	}
	return string(_s)
}
