package main

import (
	"fmt"
)

func main() {
	heights := []int{6, 7, 5, 2, 4, 5, 9, 3}
	c := []int{2, 3, 4, 5, 6}
	c = append(c, 9)
	c = []int{}
	result := largestRectangleArea(heights)
	fmt.Println(result)

}
func largestRectangleArea(heights []int) int {
	n := len(heights)
	if n == 0 {
		return 0
	}
	left := make([]int, n)
	right := make([]int, n)
	mono_stack := []int{}
	for i := 0; i < n; i++ {
		for len(mono_stack) != 0 && heights[mono_stack[len(mono_stack)-1]] >= heights[i] {
			mono_stack = mono_stack[:len(mono_stack)-1]
		}
		if len(mono_stack) > 0 {
			left[i] = mono_stack[len(mono_stack)-1]
		} else {
			left[i] = -1
		}
		mono_stack = append(mono_stack, i)
	}
	mono_stack = []int{}
	for i := n - 1; i >= 0; i-- {
		for len(mono_stack) != 0 && heights[mono_stack[len(mono_stack)-1]] >= heights[i] {
			mono_stack = mono_stack[:len(mono_stack)-1]
		}
		if len(mono_stack) > 0 {
			right[i] = mono_stack[len(mono_stack)-1]
		} else {
			right[i] = n
		}
		mono_stack = append(mono_stack, i)
	}
	result := 0
	for i := 0; i < n; i++ {
		result = max(result, (right[i]-left[i]-1)*heights[i])
	}
	return result
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
