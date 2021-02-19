
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
	left := make([]int, n)
	right := make([]int, n)
	result := make([]int, n)
	left[0] = 1
	right[n-1] = 1
	for i := 1; i < n; i++ {
		left[i] = left[i-1] * nums[i-1]
	}
	for i := n - 2; i >= 0; i-- {
		right[i] = right[i+1] * nums[i+1]
	}
	for i := 0; i < n; i++ {
		result[i] = left[i] * right[i]
	}
	return result
}

