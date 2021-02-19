package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "12[a]12[bc]"
	result := decodeString(s)
	fmt.Println(result)
}

var (
	src string
	ptr int
)

func decodeString(s string) string {
	src = s
	ptr = 0
	return getString()
}

func getString() string {
	if ptr == len(src) || src[ptr] == ']' {
		return ""
	}
	repeat := 1
	result := ""
	current := src[ptr]
	if current >= '0' && current <= '9' {
		repeat = getDigits()
		ptr++
		s := getString()
		ptr++
		result = strings.Repeat(s, repeat)
	} else if current >= 'a' && current <= 'z' || current >= 'A' && current <= 'Z' {
		result = string(current)
		ptr++
	}
	return result + getString()

}

func getDigits() int {
	ret := 0
	for ; src[ptr] >= '0' && src[ptr] <= '9'; ptr++ {
		ret = ret*10 + int(src[ptr]-'0')
	}
	return ret
}
