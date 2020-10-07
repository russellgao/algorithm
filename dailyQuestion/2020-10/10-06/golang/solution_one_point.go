package main

import (
	"fmt"
)

func main() {
	nums := []int{2, 0, 2, 1, 1, 0}
	sortColors(nums)
	fmt.Println(nums)
}

func sortColors(nums []int) {
	n := len(nums)
	ptr := 0
	for i := 0; i < n; i++ {
		if nums[i] == 0 {
			nums[i], nums[ptr] = nums[ptr], nums[i]
			ptr++
		}
	}
	for i := 0; i < n; i++ {
		if nums[i] == 1 {
			nums[i], nums[ptr] = nums[ptr], nums[i]
			ptr++
		}
	}
}
