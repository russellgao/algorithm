package main

import "fmt"

func main() {
	a1 := [][]int{[]int{1, 1, 0}, []int{1, 0, 1}, []int{0, 0, 0}}
	a2 := ac(a1)

	fmt.Println(a2)
}

func ac(A [][]int) [][]int {
	if len(A) == 0 {
		return A
	}
	m := len(A)
	n := len(A[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n>>1; j++ {
			A[i][j], A[i][n-j-1] = A[i][n-j-1], A[i][j]
		}
		for j := 0; j < n; j++ {
			A[i][j] ^= 1
		}
	}
	return A
}
