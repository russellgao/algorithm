package main

import (
	"fmt"
)

func main() {

	result := canPartition([]int{1, 5, 11, 5})
	fmt.Println(result)
}

func canPartition(nums []int) bool {
	n := len(nums)
	if n < 2 {
		return false
	}
	sum, max := 0, 0
	for _, k := range nums {
		sum += k
		if k > max {
			max = k
		}
	}
	if sum%2 != 0 {
		return false
	}
	target := sum >> 1
	if max > target {
		return false
	}
	dp := make([]bool, target+1)
	dp[0] = true
	for i := 0; i < n; i++ {
		v := nums[i]
		for j := target; j >= v; j-- {
			dp[j] = dp[j] || dp[j-v]
		}
	}
	return dp[target]
}
