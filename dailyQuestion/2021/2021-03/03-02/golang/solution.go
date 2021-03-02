package main

import "fmt"

func main() {
	nums := [][]int{[]int{1, 2, 3, 4, 5}, []int{6, 7, 8, 9, 10},
		[]int{11, 12, 13, 14, 15}, []int{16, 17, 18, 19, 20},
		[]int{21, 22, 23, 24, 25},
	}
	numarray := Constructor(nums)
	fmt.Println(numarray.SumRegion(1, 1, 2, 2))

}

type NumMatrix struct {
	sums [][]int
}

func Constructor(matrix [][]int) NumMatrix {
	m := len(matrix)
	if m == 0 {
		return NumMatrix{}
	}
	n := len(matrix[0])
	sums := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		sums[i] = make([]int, n+1)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			sums[i+1][j+1] = sums[i+1][j] + sums[i][j+1] - sums[i][j] + matrix[i][j]
		}
	}
	return NumMatrix{sums: sums}
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	return this.sums[row2+1][col2+1] - this.sums[row1][col2+1] - this.sums[row2+1][col1] + this.sums[row1][col1]
}
