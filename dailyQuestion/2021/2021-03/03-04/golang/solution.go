package main

import (
	"fmt"
	"sort"
)

func main() {
	nums := [][]int{[]int{5, 4}, []int{6, 4}, []int{6, 7}, []int{2, 3}}
	res := maxEnvelopes(nums)
	fmt.Println(res)

}

func maxEnvelopes(envelopes [][]int) (res int) {
	n := len(envelopes)
	if n == 0 {
		return
	}
	sort.Slice(envelopes, func(i, j int) bool {
		return envelopes[i][0] < envelopes[j][0] || envelopes[i][0] == envelopes[j][0] && envelopes[i][1] > envelopes[j][1]
	})

	dp := make([]int, n)
	for i := 0; i < n; i++ {
		dp[i] = 1
		for j := 0; j < i; j++ {
			if envelopes[i][1] > envelopes[j][1] {
				dp[i] = max(dp[i], dp[j]+1)
			}
		}
		if res < dp[i] {
			res = dp[i]
		}
	}

	return
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
