package main

import "fmt"

func findRepeatNumber(nums []int) int {
	tmp := map[int]bool{}
	for _, item := range nums {
		if tmp[item] {
			return item
		} else {
			tmp[item] = true
		}
	}
	return 0
}

func main() {
	nums := []int{2, 3, 1, 0, 2, 5, 3}
	result := findRepeatNumber(nums)
	fmt.Println(result)
}
