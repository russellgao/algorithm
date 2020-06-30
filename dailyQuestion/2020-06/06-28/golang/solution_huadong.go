package main

import (
	"fmt"
	"math"
)

func minSubArrayLen(s int, nums []int) int {
	n := len(nums)
	if n == 0 {
		return 0
	}
	start, end, result := 0, 0, math.MaxInt32
	sum := 0
	for end < n {
		sum += nums[end]
		for sum >= s {
			result = min(result, end-start+1)
			sum -= nums[start]
			start++
		}
		end++
	}
	if result == math.MaxInt32 {
		return 0
	}
	return result
}

func min(x, y int) int {
	if x > y {
		return y
	}
	return x
}
func main() {
	s := 7
	nums := []int{2, 3, 1, 2, 4, 3}
	result := minSubArrayLen(s, nums)
	fmt.Println(result)

}
