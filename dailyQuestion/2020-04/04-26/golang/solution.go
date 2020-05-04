package main

import "fmt"

func main() {
	a := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	b := maxSubArray(a)
	fmt.Println(b)
}

// 方法一
// 动态规划
func maxSubArray(nums []int) int {
	max := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i]+nums[i-1] > nums[i] {
			nums[i] = nums[i] + nums[i-1]
		}
		if nums[i] > max {
			max = nums[i]
		}
	}
	return max
}

// 方法二
// 分治法


func maxSubArray_2(nums []int) int {
	return get(nums, 0, len(nums)-1).mSum
}

func pushUp(left, right Status) Status {
	iSum := left.iSum + right.iSum
	lSum := max(left.lSum, left.iSum+right.lSum)
	rSum := max(right.rSum, right.iSum+left.rSum)
	mSum := max(max(left.mSum, right.mSum), left.rSum+right.lSum)
	return Status{iSum: iSum, lSum: lSum, rSum: rSum, mSum: mSum}
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func get(nums []int, left, right int) Status {
	if left == right {
		return Status{lSum: nums[left], rSum: nums[left], mSum: nums[left], iSum: nums[left]}
	}
	m := (left + right) >> 1
	lSub := get(nums, left, m)
	rSub := get(nums, m+1, right)
	return pushUp(lSub, rSub)
}

type Status struct {
	lSum, rSum, mSum, iSum int
}


