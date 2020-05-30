package main

import (
	"fmt"
)

func main() {
	heights := []int{6, 7, 5, 2, 4, 5, 9, 3}
	result := largestRectangleArea(heights)
	fmt.Println(result)

}

func largestRectangleArea(heights []int) int {
	result := 0
	n := len(heights)
	for i := 0; i < n; i++ {
		left, right := i, i
		for ; left-1 >= 0 && heights[left-1] >= heights[i]; left-- {

		}
		for ; right+1 < n && heights[right+1] > heights[i]; right++ {

		}
		result = max(result, (right-left+1)*heights[i])
	}
	return result
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
