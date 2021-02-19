package main

import (
	"fmt"
	"sort"
)

func main() {
	result := combinationSum2([]int{10, 1, 2, 7, 6, 1, 5}, 8)
	fmt.Println(result)
}

func combinationSum2(candidates []int, target int) (result [][]int) {
	sort.Ints(candidates)
	var freq [][2]int
	for _, num := range candidates {
		if freq == nil || num != freq[len(freq)-1][0] {
			freq = append(freq, [2]int{num, 1})
		} else {
			freq[len(freq)-1][1]++
		}
	}

	temp := []int{}
	var dfs func(target, idx int)
	dfs = func(target, idx int) {
		if target == 0 {
			comb := make([]int, len(temp))
			copy(comb, temp)
			result = append(result, comb)
			return
		}
		if idx == len(freq) || target < freq[idx][0] {
			return
		}
		dfs(target, idx+1)
		most := min(target/freq[idx][0], freq[idx][1])
		for i := 1; i <= most; i++ {
			temp = append(temp, freq[idx][0])
			dfs(target-i*freq[idx][0], idx+1)
		}
		temp = temp[:len(temp)-most]
	}
	dfs(target, 0)
	return
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
