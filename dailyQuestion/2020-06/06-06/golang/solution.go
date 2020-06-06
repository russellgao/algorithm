package main

import (
	"fmt"
)

func main() {

	s := []int{100, 4, 200, 1, 3, 2}
	result := longestConsecutive(s)
	fmt.Println(result)

}

func longestConsecutive(nums []int) int {
	longest := 0
	numSet := map[int]bool{}
	for _, i := range nums {
		numSet[i] = true
	}
	for num := range numSet {
		if !numSet[num-1] {
			current := num
			current_len := 1
			for numSet[current+1] {
				current++
				current_len++
			}
			longest = max(longest, current_len)
		}
	}
	return longest
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
