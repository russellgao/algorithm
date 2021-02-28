package main

import (
	"fmt"
)

func main() {
	A := []int{1, 2, 3, 4, 5, 6, 4, 54, 3, 6}
	res := isMonotonic(A)
	fmt.Println(res)
}
func isMonotonic(A []int) bool {
	isAdd := true
	isReduce := true
	for i := 0; i < len(A)-1; i++ {
		if A[i] > A[i+1] {
			isAdd = false
		}
		if A[i] < A[i+1] {
			isReduce = false
		}
	}
	return isAdd || isReduce
}
