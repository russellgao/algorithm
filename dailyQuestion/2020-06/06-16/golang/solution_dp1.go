package main

import "fmt"

func main() {
	A := [][]int{[]int{1, 3, 1}, []int{1, 5, 1}, []int{4, 2, 1}}
	result := minPathSum(A)
	fmt.Println(result)
}

func minPathSum(grid [][]int) int {
	m := len(grid)
	if m == 0 {
		return 0
	}
	n := len(grid[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 && j == 0 {
				continue
			} else if j == 0 {
				grid[i][j] = grid[i][j] + grid[i-1][j]
			} else if i == 0 {
				grid[i][j] = grid[i][j] + grid[i][j-1]
			} else {
				grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
			}
		}
	}
	return grid[m-1][n-1]
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
