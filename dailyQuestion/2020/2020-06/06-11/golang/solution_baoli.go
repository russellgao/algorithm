package main

import "fmt"

func main() {

	T := []int{73, 74, 75, 71, 69, 72, 76, 73}
	result := dailyTemperatures(T)
	fmt.Println(result)

}

func dailyTemperatures(T []int) []int {
	n := len(T)
	result := make([]int, n)
	if n == 1 {
		return result
	}
	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			if T[j] > T[i] {
				result[i] = j - i
				break
			}
		}
	}
	return result
}
