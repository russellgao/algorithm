package main

import "fmt"

func main() {
	A := []int{8, 1, 5, 2, 6}
	result := maxScoreSightseeingPair(A)
	fmt.Println(result)

}

func maxScoreSightseeingPair(A []int) int {
	result := 0
	mx := A[0]
	for j := 1; j < len(A); j++ {
		if A[j]-j+mx > result {
			result = A[j] - j + mx
		}
		if A[j]+j > mx {
			mx = A[j] + j
		}
	}
	return result
}
