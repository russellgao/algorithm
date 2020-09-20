package main

import (
	"fmt"
	"sort"
)

func main() {
	result := permuteUnique([]int{2, 1, 1})
	fmt.Println(result)
}

func permuteUnique(nums []int) (result [][]int) {
	sort.Ints(nums)
	temp := []int{}
	n := len(nums)
	visited := make([]bool, n)
	var dfs func(idx int)
	dfs = func(idx int) {
		if idx == n {
			result = append(result, append([]int(nil), temp...))
			return
		}
		for i := 0; i < n; i++ {
			if visited[i] || i > 0 && nums[i] == nums[i-1] && !visited[i-1] {
				continue
			}
			temp = append(temp, nums[i])
			visited[i] = true
			dfs(idx + 1)
			visited[i] = false
			temp = temp[:len(temp)-1]
		}
	}
	dfs(0)
	return
}
