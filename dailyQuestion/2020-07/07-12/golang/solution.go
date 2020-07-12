package main

import (
	"fmt"
	"math"
)

func calculateMinimumHP(dungeon [][]int) int {
	m := len(dungeon)
	n := len(dungeon[0])
	dp := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		dp[i] = make([]int, n+1)
		for j := 0; j < n+1; j++ {
			dp[i][j] = math.MaxInt32
		}
	}
	dp[m-1][n] = 1
	dp[m][n-1] = 1
	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			dp[i][j] = max(min(dp[i+1][j], dp[i][j+1])-dungeon[i][j], 1)
		}
	}
	return dp[0][0]

}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	dungeon := [][]int{[]int{-2, -3, 3},
		[]int{-5, -10, 1},
		[]int{10, 30, -5}}
	result := calculateMinimumHP(dungeon)
	fmt.Println(result)
}
