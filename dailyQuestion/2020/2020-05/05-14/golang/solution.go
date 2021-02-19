package main

import "fmt"

func main() {
	nums := []int{1, 2, 3, 4, 5, 4, 1, 2}
	fmt.Println(singleNumber(nums))
}

func singleNumber(nums []int) int {
	result := 0
	for _, i := range nums {
		result ^= i
	}
	return result
}
