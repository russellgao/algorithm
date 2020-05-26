package main

import (
	"fmt"
)

func main() {
	s := []int{1, 3, 4, 2, 1}
	result := findDuplicate(s)
	fmt.Println(result)

}

// 位运算
func findDuplicate(nums []int) int {
	n := len(nums)
	bit_max := 32
	for (n-1)>>bit_max == 0 {
		bit_max--
	}
	result := 0
	for bit := 0; bit <= bit_max; bit++ {
		x, y := 0, 0
		for i := 0; i < n; i++ {
			if nums[i]&(1<<bit) > 0 {
				x++
			}
			if n >= 1 && (i&(1<<bit) > 0) {
				y++
			}
		}
		if x > y {
			result |= (1 << bit)
		}
	}
	return result
}
