package main

import (
	"fmt"
	"math"
)

func subSort(array []int) []int {
	n := len(array)
	first := -1
	last := -1
	if n == 0 || n == 1 {
		return []int{first, last}
	}
	min_n := math.MaxInt32
	max_n := math.MinInt32
	for i := 0; i < n; i++ {
		if array[i] >= max_n {
			max_n = array[i]
		} else {
			last = i
		}
		if array[n-1-i] <= min_n {
			min_n = array[n-1-i]
		} else {
			first = n - i - 1
		}
	}
	return []int{first, last}
}

func main() {
	array := []int{1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19}
	result := subSort(array)
	fmt.Println(result)
}
