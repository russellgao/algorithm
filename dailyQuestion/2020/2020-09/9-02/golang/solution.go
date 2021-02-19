package main

import (
	"fmt"
)

func main() {
	result := removeDuplicates([]int{1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7})
	fmt.Println(result)
}

func removeDuplicates(nums []int) int {
	n := len(nums)
	if n < 2 {
		return n
	}
	i := 1
	for j := 1; j < n; j++ {
		if nums[j] != nums[j-1] {
			nums[i] = nums[j]
			i++
		}
	}
	return i
}
