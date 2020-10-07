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
	p0, p1 := 0, 0
	for i := 0; i < n; i++ {
		if nums[i] == 1 {
			nums[i], nums[p1] = nums[p1], nums[i]
			p1++
		} else if nums[i] == 0 {
			nums[i], nums[p0] = nums[p0], nums[i]
			if p0 < p1 {
				nums[i], nums[p1] = nums[p1], nums[i]
			}
			p0++
			p1++
		}
	}
}
