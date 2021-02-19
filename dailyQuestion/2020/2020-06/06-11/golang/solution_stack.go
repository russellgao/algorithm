package main

import "fmt"

func main() {

	T := []int{73, 74, 75, 71, 69, 72, 76, 73}
	result := dailyTemperatures(T)
	fmt.Println(result)

}

func dailyTemperatures(T []int) []int {
	n := len(T)
	result := make([]int, n)
	stack := []int{}
	for i := 0; i < n; i++ {
		for len(stack) != 0 && T[stack[len(stack)-1]] < T[i] {
			result[stack[len(stack)-1]] = i - stack[len(stack)-1]
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i)
	}
	return result
}

