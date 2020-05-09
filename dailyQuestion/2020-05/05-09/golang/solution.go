package main

import (
	"fmt"
	"math"
)

func main() {
	x := 5
	fmt.Println(mySqrt3(x))
}

// 珍珠计算器法
func mySqrt1(x int) int {
	if x == 0 {
		return 0
	}
	result := int(math.Exp(0.5 * math.Log(float64(x))))
	if (result+1)*(result+1) <= x {
		return result + 1
	}
	return result
}

// 二分法
func mySqrt2(x int) int {
	left, right, result := 0, x, -1
	for left <= right {
		mid := (left + right) >> 1
		if mid*mid <= x {
			result = mid
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return result
}

// 牛顿法
func mySqrt3(x int) int {
	if x == 0 {
		return 0
	}
	c, x0 := float64(x), float64(x)
	for {
		xi := 0.5 * (x0 + c/x0)
		if math.Abs(x0-xi) < 1e-7 {
			break
		}
		x0 = xi
	}
	return int(x0)
}
