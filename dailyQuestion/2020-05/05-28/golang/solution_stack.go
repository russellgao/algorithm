package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	s := "100[leetcode]"
	result := decodeString(s)
	fmt.Println(result)

}

func decodeString(s string) string {
	stack := []string{}
	for i := 0; i < len(s); i++ {
		if s[i] != ']' {
			stack = append(stack, string(s[i]))
		} else {
			tmp_s := ""
			for {
				stack_len := len(stack)
				if stack[stack_len-1] != "[" {
					tmp_s = stack[stack_len-1] + tmp_s
					stack = stack[:stack_len-1]
				} else {
					break
				}
			}
			stack = stack[:len(stack)-1]
			repeat := ""
			for {
				stack_len := len(stack)
				if stack_len > 0 && stack[stack_len-1] >= "0" && stack[stack_len-1] <= "9" {
					repeat = stack[stack_len-1] + repeat
					stack = stack[:stack_len-1]
				} else {
					break
				}
			}
			_o, _ := strconv.ParseInt(repeat, 10, 64)
			_repeat := int(_o)
			tmp_t := strings.Repeat(tmp_s, _repeat)
			stack = append(stack, tmp_t)
		}
	}
	return strings.Join(stack, "")
}


