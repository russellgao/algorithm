package main

import (
	"fmt"
	"strconv"
)

func main() {
	tokens := []string{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}
	res := evalRPN(tokens)
	fmt.Println(res)
}

func evalRPN(tokens []string) int {
	stack := []int{}
	for i := 0; i < len(tokens); i++ {
		tmp := tokens[i]
		switch tmp {
		case "+":
			num1 := stack[len(stack)-1]
			num2 := stack[len(stack)-2]
			stack = stack[:len(stack)-2]
			stack = append(stack, num2+num1)
		case "-":
			num1 := stack[len(stack)-1]
			num2 := stack[len(stack)-2]
			stack = stack[:len(stack)-2]
			stack = append(stack, num2-num1)
		case "*":
			num1 := stack[len(stack)-1]
			num2 := stack[len(stack)-2]
			stack = stack[:len(stack)-2]
			stack = append(stack, num2*num1)
		case "/":
			num1 := stack[len(stack)-1]
			num2 := stack[len(stack)-2]
			stack = stack[:len(stack)-2]
			stack = append(stack, num2/num1)
		default:
			num, _ := strconv.Atoi(tmp)
			stack = append(stack, num)
		}
	}
	return stack[0]
}
