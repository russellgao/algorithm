package main

import "fmt"

func main() {
	a1 := [][]int{[]int{1, 1, 0}, []int{1, 0, 1}, []int{0, 0, 0}}
	a2 := flipAndInvertImage(a1)

	fmt.Println(a2)
}

func flipAndInvertImage(A [][]int) [][]int {
	for _, row := range A {
		left, right := 0, len(row)-1
		for left < right {
			if row[left] == row[right] {
				row[left] ^= 1
				row[right] ^= 1
			}
			left++
			right--
		}
		if left == right {
			row[left] ^= 1
		}
	}
	return A
}
