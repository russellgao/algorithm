package main

import "fmt"

func main() {
	a := []int{2, 3, 1, 1, 5}
	b := jump(a)
	fmt.Println(b)
}

// 方法一
// 反向查找出发位置
func jump(nums []int) int {
	position := len(nums) - 1
	steps := 0
	for position > 0 {
		for i := 0; i < position; i++ {
			// 从i个位置可以跳到position ，并且可以保证下标i是最小的一个
			if i+nums[i] >= position {
				position = i
				steps++
				break
			}
		}
	}
	return steps
}


// 方法二
// 正向寻找，通过局部最优达到全局最优
func jump_2(nums []int) int {
	length := len(nums)
	end := 0
	maxPosition := 0
	steps := 0
	for i := 0; i < length-1; i++ {
		// 当前位置和吓一跳可以跳到的最远位置
		maxPosition = max(maxPosition, i+nums[i])
		// 判断是否到了下一次跳跃的时候
		if i == end {
			end = maxPosition
			steps++
		}
	}
	return steps
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
