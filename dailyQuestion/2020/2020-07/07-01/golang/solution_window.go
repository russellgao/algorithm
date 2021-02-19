package main

import "fmt"

func findLength(A []int, B []int) int {
	m := len(A)
	n := len(B)
	result := 0
	var maxLength func(addA, addB, length int) int
	maxLength = func(addA, addB, length int) int {
		ret := 0
		k := 0
		for i := 0; i < length; i++ {
			if A[addA+i] == B[addB+i] {
				k++
				ret = max(ret, k)
			} else {
				k = 0
			}
		}
		return ret
	}

	for i := 0; i < m; i++ {
		length := min(n, m-i)
		result = max(result, maxLength(i, 0, length))
	}
	for i := 0; i < n; i++ {
		length := min(m, n-i)
		result = max(result, maxLength(0, i, length))
	}

	return result
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	A := []int{1, 2, 3, 2, 1}
	B := []int{3, 2, 1, 4, 7}
	result := findLength(A, B)
	fmt.Println(result)
}
