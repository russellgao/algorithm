package main

import "fmt"

func main() {
	a := []int{1, 9, 2, 8, 3, 7, 4, 5}
	quick_sort(a)
	fmt.Println(a)
}

// 快速排序
func quick_sort(list []int) {
	sort(list, 0, len(list)-1)
}

// 定义递归函数
func sort(list []int, left, right int) {
	if left < right {
		// 取基数为第一个值
		key := list[left]

		// 左右指针
		i := left
		j := right
		for i < j {

			// 寻找复合条件的一个交换，即右边小于key，左边大于key
			for i < j && list[j] >= key {
				j--
			}
			for i < j && list[i] <= key {
				i++
			}
			list[i], list[j] = list[j], list[i]
		}
		// 把第一个基数交换到i位置，使得左边都小于key ，右边都大于k
		list[left], list[i] = list[i], list[left]
		// 对左边进行快排
		sort(list, left, i-1)
		// 对右边尽心快排
		sort(list, i+1, right)
	}
}
