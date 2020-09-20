package main

import (
	"fmt"
)

func main() {
	result := countNumbersWithUniqueDigits(2)
	fmt.Println(result)
}

func countNumbersWithUniqueDigits(n int) int {
	if n == 0 {
		return 1
	}
	var dfs func(idx int) int
	used := make([]bool, 10)
	dfs = func(idx int) int {
		result := 0
		if idx == n {
			return 0
		}
		for num := 0; num < 10; num++ {
			// 剪枝：多位数时，第一个数字不能为0
			if n >= 2 && idx == 1 && num == 0 {
				continue
			}
			// 剪枝：不能使用用过的数字
			if used[num] {
				continue
			}
			used[num] = true
			result += dfs(idx+1) + 1
			used[num] = false
		}
		return result
	}
	return dfs(0)
}
