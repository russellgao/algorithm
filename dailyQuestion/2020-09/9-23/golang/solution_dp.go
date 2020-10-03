package main

import (
	"fmt"
	"math"
)

func main() {
	result := minimumOperations("rrryyyrryyyrr")
	fmt.Println(result)
}

const inf = math.MaxInt32

func minimumOperations(leaves string) int {
	n := len(leaves)
	f := make([][3]int, n)
	f[0][0] = boolToInt(leaves[0] == 'y')
	f[0][1] = inf
	f[0][2] = inf
	f[1][2] = inf
	for i := 1; i < n; i++ {
		f[i][0] = f[i-1][0] + boolToInt(leaves[i] == 'y')
		f[i][1] = min(f[i-1][0], f[i-1][1]) + boolToInt(leaves[i] == 'r')
		if i >= 2 {
			f[i][2] = min(f[i-1][1], f[i-1][2]) + boolToInt(leaves[i] == 'y')
		}
	}
	return f[n-1][2]
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func boolToInt(b bool) int {
	if b {
		return 1
	}
	return 0
}
