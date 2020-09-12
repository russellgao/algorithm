package main

import "fmt"

func main() {
	result := combine(4, 2)

	fmt.Println(result)
}

func combine(n int, k int) (result [][]int) {
	temp := []int{}
	var dfs func(cur int)
	dfs = func(cur int) {
		if len(temp)+(n-cur+1) < k {
			return
		}
		if len(temp) == k {
			comb := make([]int, k)
			copy(comb, temp)
			result = append(result, comb)
			return
		}
		temp = append(temp, cur)
		dfs(cur + 1)
		temp = temp[:len(temp)-1]
		dfs(cur + 1)
	}
	dfs(1)
	return
}
