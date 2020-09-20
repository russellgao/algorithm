package main

import (
	"fmt"
)

func main() {
	result := countNumbersWithUniqueDigits(2)
	fmt.Println(result)
}

func countNumbersWithUniqueDigits(n int) int {
	if n == 0 {
		return 1
	}
	first, second := 10, 9
	for i := 1; i < n; i++ {
		second *= 10 - i
		first += second
	}
	return first
}
