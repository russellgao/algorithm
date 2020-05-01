package main

import "fmt"

func main() {

	a := "abcdefg"
	c := reverseString(a)
	fmt.Println(c)
}

// 字符串递归调用进行反转
func reverseString(str1 string) string {
	if str1 == "" {
		return ""
	}
	if len(str1) == 1 {
		return str1
	}
	result := reverseString(str1[1:]) + string(str1[0])
	return result

}
