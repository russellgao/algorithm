package main

import (
	"fmt"
	"strconv"
)

func multiply(num1 string, num2 string) string {
	if num1 == "0" || num2 == "0" {
		return "0"
	}
	result := "0"
	for j := len(num2) - 1; j >= 0; j-- {
		jin := 0
		he := ""
		for i := len(num1) - 1; i >= 0; i-- {
			item := int(num1[i]-'0')*int(num2[j]-'0') + jin

			he = strconv.Itoa(item%10) + he
			jin = item / 10
		}
		if jin != 0 {
			he = strconv.Itoa(jin) + he
		}
		he = add0(he, len(num2)-1-j)
		result = addStrings(result, he)
	}
	return result
}

func add0(he string, index int) string {
	for i := 0; i < index; i++ {
		he += "0"
	}
	return he
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

func main() {
	num1 := "123"
	num2 := "456"
	result := multiply(num1, num2)
	fmt.Println(result)
}
