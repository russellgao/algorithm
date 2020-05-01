package main

import "fmt"

func main() {

	a := []string{"a", "b", "c", "d", "e", "f"}
	reverseLists(a)
	fmt.Println(a)
}

// 字符串列表递归调用进行反转
func reverseLists(list1 []string) {
	helper(list1, 0, len(list1)-1)
}

func helper(list1 []string, left, right int) {
	if left < right {
		list1[left], list1[right] = list1[right], list1[left]
		helper(list1, left+1, right-1)
	}
}
