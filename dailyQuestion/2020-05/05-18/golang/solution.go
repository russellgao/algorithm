package main

import (
	"fmt"
	"math"
)

func main() {
	a := []int{2, 3, -2, 4}

	b := maxProduct(a)

	fmt.Println(b)
}

// 动态规划
func maxProduct(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	nums_min := nums[0]
	nums_max := nums[0]
	result := nums[0]
	for i := 1; i < len(nums); i++ {
		a := nums_min
		b := nums_max
		nums_min = min(nums[i], nums[i]*a, nums[i]*b)
		nums_max = max(nums[i], nums[i]*a, nums[i]*b)
		if nums_max > result {
			result = nums_max
		}
	}
	return result
}

func max(a, b, c int) int {
	if a > b {
		if a > c {
			return a
		}
		return c
	}
	if b > c {
		return b
	}
	return c
}

func min(a, b, c int) int {
	if a > b {
		if c > b {
			return b
		}
		return c
	}
	if a > c {
		return c
	}
	return a
}

// 暴力求解
func maxProduct2(nums []int) int {
	result := math.MinInt64
	for i := 0; i < len(nums); i++ {
		tmp := 1
		for j := i; j >= 0; j-- {
			tmp *= nums[j]
			if tmp > result {
				result = tmp
			}
		}
	}
	return result
}
