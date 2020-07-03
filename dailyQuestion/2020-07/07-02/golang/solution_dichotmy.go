package main

import (
	"fmt"
)

func kthSmallest(matrix [][]int, k int) int {
	n := len(matrix)
	var check func(mid int) bool
	check = func(mid int) bool {
		num := 0
		i, j := n-1, 0
		for i >= 0 && j < n {
			if matrix[i][j] <= mid {
				num += i + 1
				j++
			} else {
				i--
			}
		}
		return num >= k
	}

	left := matrix[0][0]
	right := matrix[n-1][n-1]
	for left < right {
		mid := (left + right) >> 1
		if check(mid) {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left
}

func main() {
	matrix := [][]int{[]int{1, 5, 9}, []int{10, 11, 13}, []int{12, 13, 15}}
	result := kthSmallest(matrix, 8)
	fmt.Println(result)
}
