package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 4, 5}
	b := 2
	c := find_num(a, b)
	fmt.Println(c)
}

// 二分法查找key 对应的下表，不存在则返回 -1
func find_num(nums []int, key int) int {
	left := 0
	right := len(nums) - 1
	for left <= right {
		mid := (left + right) >> 1
		if nums[mid] == key {
			return mid
		}
		if nums[mid] > key {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return -1
}