package main

import "fmt"

func findLength(A []int, B []int) int {
	len_A := len(A)
	len_B := len(B)
	result := 0
	for i := 0; i < len_A; i++ {
		for j := 0; j < len_B; j++ {
			k := 0
			for i+k < len_A && j+k < len_B && A[i+k] == B[j+k] {
				k++
			}
			if k > result {
				result = k
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
