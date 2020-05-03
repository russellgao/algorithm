package main

import "fmt"

func main() {
	a := []int{1, 9, 2, 8, 3, 7, 4, 5}
	c := merge_sort(a)
	fmt.Println(c)
}

// 归并排序
func merge_sort(list []int) []int {
	if len(list) == 1 {
		return list
	}
	mid := len(list) >> 1
	left := merge_sort(list[:mid])
	right := merge_sort(list[mid:])
	return merge(left, right)
}

// 合并两个有序数组
func merge(list1, list2 []int) []int {
	tmp := []int{}
	i, j := 0, 0
	for i < len(list1) && j < len(list2) {
		if list1[i] < list2[j] {
			tmp = append(tmp, list1[i])
			i += 1
		} else {
			tmp = append(tmp, list2[j])
			j += 1
		}
	}
	if i == len(list1) {
		tmp = append(tmp, list2[j:]...)
	} else if j == len(list2) {
		tmp = append(tmp, list1[i:]...)
	}
	return tmp
}
