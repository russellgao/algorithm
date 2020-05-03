package main

import "fmt"

func main() {
	a := []int{1, 9, 2, 8, 3, 7, 4, 5}
	bubble_sort(a)
	fmt.Println(a)
}

// 冒泡排序
func bubble_sort(list []int) {
	for i := 0; i < len(list); i++ {
		for j := i; j < len(list); j++ {
			if list[i] > list[j] {
				list[i], list[j] = list[j], list[i]
			}
		}
	}
}
