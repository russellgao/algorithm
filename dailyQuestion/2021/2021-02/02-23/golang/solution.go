package main

import "fmt"

func main() {
	customers := []int{1, 0, 1, 2, 1, 1, 7, 5}
	grumpy := []int{0, 1, 0, 1, 0, 1, 0, 1}
	X := 3

	//customers := []int{5, 8}
	//grumpy := []int{0, 1}
	//X := 1

	res := maxSatisfied(customers, grumpy, X)
	fmt.Println(res)
}

// customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3

func maxSatisfied(customers []int, grumpy []int, X int) (res int) {
	n := len(customers)
	for i := 0; i < n; i++ {
		if grumpy[i] == 0 {
			res += customers[i]
		}
	}
	_sum := 0
	for i := 0; i < X; i++ {
		if grumpy[i] == 1 {
			_sum += customers[i]
		}
	}
	tmp_sum := _sum
	for i := X; i < n; i++ {
		if grumpy[i] == 1 {
			tmp_sum += customers[i]
		}
		if grumpy[i-X] == 1 {
			tmp_sum -= customers[i-X]
		}
		_sum = max(_sum, tmp_sum)
	}
	res += _sum
	return
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
