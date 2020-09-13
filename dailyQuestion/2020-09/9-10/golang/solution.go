package main

import "fmt"

func main() {
	result := combinationSum3(3, 8)
	fmt.Println(result)
}

func combinationSum3(k int, n int) (result [][]int) {
	temp := []int{}

	var dfs func(target, idx int)
	dfs = func(target, idx int) {
		if target == 0 && len(temp) == k {
			comb := make([]int, k)
			copy(comb, temp)
			result = append(result, comb)
			return
		}
		if target <= 0 || len(temp) >= k {
			return
		}
		if idx < 10 {
			dfs(target, idx+1)
			temp = append(temp, idx)
			dfs(target-idx, idx+1)
			temp = temp[:len(temp)-1]
		}

	}
	dfs(n, 1)
	return
}
