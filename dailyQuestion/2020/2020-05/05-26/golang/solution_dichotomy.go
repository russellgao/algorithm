package main

import (
	"fmt"
)

func main() {
	s := []int{1, 3, 4, 2, 1}
	result := findDuplicate(s)
	fmt.Println(result)

}

// 二分法求解
func findDuplicate(nums []int) int {
	n := len(nums)
	left, right := 1, n-1
	result := -1
	for left <= right {
		mid := (left + right) >> 1
		cnt := 0
		for i := 0; i < n; i++ {
			if nums[i] <= mid {
				cnt++
			}
		}
		if cnt <= mid {
			left = mid + 1
		} else {
			right = mid - 1
			result = mid
		}
	}
	return result
}
