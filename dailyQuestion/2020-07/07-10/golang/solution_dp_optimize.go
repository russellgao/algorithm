package main

import "fmt"

func maxProfit(prices []int) int {
	n := len(prices)
	if n == 0 {
		return 0
	}
	dp0 := -prices[0]
	dp1 := 0
	dp2 := 0
	for i := 1; i < n; i++ {
		_dp0 := max(dp0, dp2-prices[i])
		_dp1 := dp0 + prices[i]
		_dp2 := max(dp1, dp2)
		dp0, dp1, dp2 = _dp0, _dp1, _dp2
	}
	return max(dp1, dp2)

}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	prices := []int{1, 2, 3, 0, 2}
	result := maxProfit(prices)
	fmt.Println(result)
}
