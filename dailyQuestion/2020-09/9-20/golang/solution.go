package main

import (
	"fmt"
)

func main() {
	result := subsets([]int{2, 1, 3})
	fmt.Println(result)
}

func subsets(nums []int) (result [][]int) {
	temp := []int{}
	var dfs func(idx int)
	n := len(nums)
	dfs = func(idx int) {
		if idx == n {
			result = append(result, append([]int(nil), temp...))
			return
		}
		temp = append(temp, nums[idx])
		dfs(idx + 1)
		temp = temp[:len(temp)-1]
		dfs(idx + 1)
	}
	dfs(0)
	return
}
