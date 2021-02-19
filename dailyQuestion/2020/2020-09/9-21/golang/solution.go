package main

import "fmt"

func main() {
	result := twoSum([]int{2, 7, 11, 15}, 9)
	fmt.Println(result)
}

func twoSum(nums []int, target int) []int {
	tmp := map[int]int{}
	for i, v := range nums {
		cha := target - v
		if k, ok := tmp[cha]; ok {
			return []int{k, i}
		}
		tmp[v] = i
	}
	return nil
}
