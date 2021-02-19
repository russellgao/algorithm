package main

import (
	"fmt"
	"strconv"
)

// 如果输入的数字超过64位则不能正确返回，只能处理int64 位的数字
func addBinary(a string, b string) string {
	a1, _ := strconv.ParseInt(a, 2, 64)
	b1, _ := strconv.ParseInt(b, 2, 64)
	for b1 != 0 {
		result := a1 ^ b1
		carry := (a1 & b1) << 1
		a1 = result
		b1 = carry
	}
	return strconv.FormatInt(a1, 2)
}

func main() {
	a := "1111"
	b := "1101000100"
	result := addBinary(a, b)
	fmt.Println(result)
}

