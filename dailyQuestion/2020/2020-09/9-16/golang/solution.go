package main

import "fmt"

func main() {
	result := permute([]int{1, 2, 3})
	fmt.Println(result)
}

func permute(nums []int) (result [][]int) {
	var dfs func(cur int)
	n := len(nums)
	dfs = func(cur int) {
		if cur == n {
			p := make([]int, n)
			copy(p, nums)
			result = append(result, p)
			return
		}
		for i := cur; i < n; i++ {
			nums[i], nums[cur] = nums[cur], nums[i]
			dfs(cur + 1)
			nums[i], nums[cur] = nums[cur], nums[i]
		}

	}
	dfs(0)
	return
}
