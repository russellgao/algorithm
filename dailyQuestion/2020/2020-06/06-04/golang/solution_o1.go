package main

import (
	"fmt"
)

func main() {

	s := []int{1, 2, 3, 4}
	result := productExceptSelf(s)
	fmt.Println(result)

}

func productExceptSelf(nums []int) []int {
	n := len(nums)
	result := make([]int, n)
	result[0] = 1
	for i := 1; i < n; i++ {
		result[i] = result[i-1] * nums[i-1]
	}
	tmp := 1
	for i := n - 2; i >= 0; i-- {
		tmp *= nums[i+1]
		result[i] = result[i] * tmp
	}
	return result
}
