package main

import "fmt"

func main() {
	result := combinationSum([]int{2, 3, 6, 7}, 7)
	fmt.Println(result)
}

func combinationSum(candidates []int, target int) (result [][]int) {
	temp := []int{}
	var dfs func(target, idx int)
	dfs = func(target, idx int) {
		if idx == len(candidates) {
			return
		}
		if target == 0 {
			size := len(temp)
			comb := make([]int, size)
			copy(comb, temp)
			result = append(result, comb)
			return
		}
		dfs(target, idx+1)
		if target-candidates[idx] >= 0 {
			temp = append(temp, candidates[idx])
			dfs(target-candidates[idx], idx)
			temp = temp[:len(temp)-1]
		}
	}
	dfs(target, 0)
	return
}
