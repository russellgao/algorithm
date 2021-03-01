package main

import (
	"fmt"
)

func main() {
	nums := []int{2, 1, 7, 8, 5, 9}
	obj := Constructor(nums)
	fmt.Println(obj.SumRange(0, 4))
	fmt.Println(obj.SumRange(1, 4))
	fmt.Println(obj.SumRange(2, 4))
	fmt.Println(obj.SumRange(3, 4))
	fmt.Println(obj.SumRange(4, 4))
}

type NumArray struct {
	sums []int
}

func Constructor(nums []int) NumArray {
	sums := make([]int, len(nums)+1)
	for i := 0; i < len(nums); i++ {
		sums[i+1] = sums[i] + nums[i]
	}
	return NumArray{sums}
}

func (this *NumArray) SumRange(i int, j int) int {
	return this.sums[j+1] - this.sums[i]
}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.SumRange(i,j);
 */
