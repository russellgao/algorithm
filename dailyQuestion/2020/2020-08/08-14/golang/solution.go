package main

import "fmt"

func isValid(s string) bool {
	if s == "" {
		return true
	}
	if len(s)%2 == 1 {
		return false
	}
	stack := []byte{}
	pairs := map[byte]byte{'(': ')', '[': ']', '{': '}'}
	for i := 0; i < len(s); i++ {
		if len(stack) == 0 && (s[i] == '}' || s[i] == ']' || s[i] == ')') {
			return false
		}
		if _, ok := pairs[s[i]]; ok {
			stack = append(stack, s[i])
			continue
		}

		tmp := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if s[i] != pairs[tmp] {
			return false
		}
	}
	if len(stack) > 0 {
		return false
	}
	return true
}

func main() {
	s := "{{}{{}{)()({}{)"
	fmt.Println(isValid(s))
}
