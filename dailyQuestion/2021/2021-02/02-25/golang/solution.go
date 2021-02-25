package main

import "fmt"

func main() {
	matrix := [][]int{
		[]int{1, 2, 3, 7},
		[]int{4, 5, 6, 9},
		[]int{7, 8, 9, 4},
	}
	res := transpose(matrix)
	fmt.Println(res)
}
func transpose(matrix [][]int) [][]int {
	m := len(matrix)
	n := len(matrix[0])
	res := make([][]int, n)
	for i := 0; i < n; i++ {
		res[i] = make([]int, m)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			res[j][i] = matrix[i][j]
		}
	}
	return res
}
