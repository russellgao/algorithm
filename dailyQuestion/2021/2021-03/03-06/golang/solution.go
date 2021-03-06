package main

import "fmt"

func main() {
	nums := []int{1, 2, 1, 7, 6, 4, 9, 8,1}
	res := nextGreaterElements(nums)

	fmt.Println(res)

}

func nextGreaterElements(nums []int) []int {
	n := len(nums)
	res := make([]int, n)
	for i := 0; i < n; i++ {
		res[i] = -1
	}
	stack := []int{}
	for i := 0; i < 2*n-1; i++ {
		for len(stack) > 0 && nums[stack[len(stack)-1]] < nums[i%n] {
			res[stack[len(stack)-1]] = nums[i%n]
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i%n)
	}
	return res
}
