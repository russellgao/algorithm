package main

import (
	"fmt"
)

func searchMatrix(matrix [][]int, target int) bool {
	m := len(matrix)
	if m == 0 {
		return false
	}
	n := len(matrix[0])
	i, j := m-1, 0
	for i >= 0 && j < n {
		if matrix[i][j] == target {
			return true
		}
		if target > matrix[i][j] {
			j++
		} else {
			i--
		}
	}
	return false
}

func main() {

	matrix := [][]int{[]int{1, 4, 7, 11, 15}, []int{2, 5, 8, 12, 19}, []int{3, 6, 9, 16, 22}, []int{10, 13, 14, 17, 24}, []int{18, 21, 23, 26, 30}}
	result := searchMatrix(matrix, 5)
	fmt.Println(result)
}
