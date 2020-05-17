package main

import "fmt"

// 位运算的常用操作

//| 或运算
func bit_or(a, b int) int {
	return a | b
}

//& 与运算
func bit_and(a, b int) int {
	return a & b
}

//^ 异或运算
func bit_yihuo_(a, b int) int {
	return a ^ b
}

//~ 取反
func bit_not(a int) int {
	return ^a
}

// 求相反数
func reversal(a int) int {
	return ^a + 1
}

// 求绝对值
func abs(a int) int {
	i := a >> 31
	return (a ^ i) - i
}

func count_1(a int) int {
	count := 0
	for a != 0 {
		a = a & (a - 1)
		count += 1
	}
	return count
}
func swap(a, b int) (int, int) {
	a ^= b
	b ^= a
	a ^= b
	return a, b
}

func main() {
	a := 5
	//b := 3
	c := bit_not(a)
	fmt.Println(c)
}
