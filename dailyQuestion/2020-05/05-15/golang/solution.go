package main

import "fmt"

func main() {
	nums := []int{3, 4, 7, 2, -3, 1, 4, 2}

	fmt.Println(subarraySum2(nums, 7))
}

// 方法一 枚举
func subarraySum1(nums []int, k int) int {
	count := 0
	for i := 0; i < len(nums); i++ {
		sum := 0
		for j := i; j >= 0; j-- {
			sum += nums[j]
			if sum == k {
				count++
			}
		}
	}
	return count
}

// 方法二
// 前缀和 + 哈希表优化
func subarraySum2(nums []int, k int) int {
	count, pre := 0, 0
	mp := map[int]int{0: 1}
	for i := 0; i < len(nums); i++ {
		pre += nums[i]
		if _, ok := mp[pre-k]; ok {
			count += mp[pre-k]
		}
		mp[pre] += 1
	}
	return count
}
