package main

import "fmt"

func missingTwo(nums []int) []int {
	n := len(nums) + 2
	sum := 0
	for _, num := range nums {
		sum += num
	}
	sumTwo := n*(n+1)/2 - sum
	limit := sumTwo / 2
	sum = 0
	for _, num := range nums {
		if num <= limit {
			sum += num
		}
	}
	one := limit*(limit+1)/2 - sum
	return []int{one, sumTwo - one}

}

func main() {
	nums := []int{3, 4, 5, 1}
	result := missingTwo(nums)
	fmt.Println(result)
}
