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
