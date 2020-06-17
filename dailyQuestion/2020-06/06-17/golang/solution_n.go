package main

import "fmt"

func main() {
	A := []int{8, 1, 5, 2, 6}
	result := maxScoreSightseeingPair(A)
	fmt.Println(result)

}

func maxScoreSightseeingPair(A []int) int {
	result := 0
	n := len(A)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			tmp := A[i] + A[j] + i - j
			if tmp > result {
				result = tmp
			}
		}
	}
	return result
}
