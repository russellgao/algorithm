package main

import (
	"fmt"
	"strconv"
)

func main() {
	num := 12258
	result := translateNum(num)
	fmt.Println(result)

}

func translateNum(num int) int {
	f_2, f_1 := 1, 1
	s := strconv.Itoa(num)
	for i := 2; i <= len(s); i++ {
		pre := s[i-2 : i]
		f := 0
		if pre >= "10" && pre <= "25" {
			f = f_1 + f_2
		} else {
			f = f_1
		}
		f_2 = f_1
		f_1 = f
	}
	return f_1
}
