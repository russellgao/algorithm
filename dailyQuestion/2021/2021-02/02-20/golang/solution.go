package main

import "fmt"

func main() {
	nums := []int{1, 2, 2, 3, 1}

	res := findShortestSubArray(nums)

	fmt.Println(res)
}

type entry struct {
	count int
	left  int
	right int
}

func findShortestSubArray(nums []int) (res int) {
	m := map[int]entry{}
	for i, v := range nums {
		if e, ok := m[v]; ok {
			e.count++
			e.right = i
			m[v] = e
		} else {
			m[v] = entry{1, i, i}
		}
	}
	maxCount := 0
	for _, v := range m {
		if v.count > maxCount {
			res = v.right - v.left + 1
			maxCount = v.count
		} else if v.count == maxCount {
			res = min(res, v.right-v.left+1)
		}
	}
	return
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
