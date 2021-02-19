package main

import "fmt"

func findLength(A []int, B []int) int {
	m := len(A)
	n := len(B)
	result := 0
	dp := make([][]int, m+1)
	for i := 0; i <= m; i++ {
		dp[i] = make([]int, n+1)
	}
	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			if A[i] == B[j] {
				dp[i][j] = dp[i+1][j+1] + 1
				if dp[i][j] > result {
					result = dp[i][j]
				}
			} else {
				dp[i][j] = 0
			}
		}
	}
	return result
}

func main() {
	A := []int{1, 2, 3, 2, 1}
	B := []int{3, 2, 1, 4, 7}
	result := findLength(A, B)
	fmt.Println(result)
}
