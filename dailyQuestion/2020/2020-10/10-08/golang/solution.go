package main

import (
	"fmt"
)

func main() {
	nums := []int{1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6}
	result := removeDuplicates(nums)
	fmt.Println(result)
}

func removeDuplicates(nums []int) int {
	i, count := 1, 1
	for j := 1; j < len(nums); j++ {
		if nums[j] == nums[j-1] {
			count++
		} else {
			count = 1
		}
		if count <= 2 {
			nums[i] = nums[j]
			i++
		}
	}
	return i
}
