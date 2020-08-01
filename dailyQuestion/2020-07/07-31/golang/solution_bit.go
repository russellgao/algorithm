package main

import "fmt"

func missingTwo(nums []int) []int {
	ret := 0
	for i, num := range nums {
		ret ^= (i + 1)
		ret ^= num
	}
	ret ^= len(nums) + 1
	ret ^= len(nums) + 2
	mask := 1
	for mask&ret == 0 {
		mask <<= 1
	}
	a, b := 0, 0
	for i := 1; i <= len(nums)+2; i++ {
		if i&mask == 0 {
			a ^= i
		} else {
			b ^= i
		}
	}
	for _, num := range nums {
		if num&mask == 0 {
			a ^= num
		} else {
			b ^= num
		}
	}
	return []int{a, b}
}

func main() {
	nums := []int{3, 4, 5, 1}
	result := missingTwo(nums)
	fmt.Println(result)
}
