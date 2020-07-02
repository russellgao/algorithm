package main

import (
	"fmt"
	"sort"
)

func kthSmallest(matrix [][]int, k int) int {
	p := []int{}
	n := len(matrix)
	for i := 0; i < n; i++ {
		p = append(p, matrix[i]...)
	}
	sort.Ints(p)
	return p[k-1]
}

func main() {
	matrix := [][]int{[]int{1, 5, 9}, []int{10, 11, 13}, []int{12, 13, 15}}
	result := kthSmallest(matrix, 8)
	fmt.Println(result)
}
