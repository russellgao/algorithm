package main

import (
	"fmt"
)

func main() {
	result := removeElement([]int{2, 3, 4, 5, 2, 4}, 2)
	fmt.Println(result)
}
func removeElement(nums []int, val int) int {
	i := 0
	for j := 0; j < len(nums); j++ {
		if nums[j] != val {
			nums[i] = nums[j]
			i++
		}
	}
	return i
}
