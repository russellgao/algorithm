package main

import "fmt"

func main() {

	num := 12258
	result := translateNum(num)
	fmt.Println(result)

}

func translateNum(num int) int {
	f_2, f_1 := 1, 1
	for num != 0 {
		pre := num % 100
		f := 0
		if pre >= 10 && pre <= 25 {
			f = f_2 + f_1
		} else {
			f = f_1
		}
		f_2 = f_1
		f_1 = f
		num /= 10
	}

	return f_1
}
