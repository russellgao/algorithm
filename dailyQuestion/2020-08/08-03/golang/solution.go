package main

import (
	"fmt"
	"strconv"
)

func main() {
	num1 := "999999"
	num2 := "999"
	result := addStrings(num1, num2)
	fmt.Println(result)

}
func addStrings(num1 string, num2 string) string {
	i, j, add := len(num1)-1, len(num2)-1, 0
	result := ""
	for i >= 0 || j >= 0 {
		if i >= 0 {
			add += int(num1[i] - '0')
			i--
		}
		if j >= 0 {
			add += int(num2[j] - '0')
			j--
		}
		result = strconv.Itoa(add%10) + result
		add /= 10
	}
	if add > 0 {
		result = strconv.Itoa(add) + result
	}
	return result
}
