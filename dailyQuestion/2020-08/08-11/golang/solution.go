package main

import (
	"fmt"
)

func replaceSpace(s string) string {
	n := len(s)
	bs := make([]byte, n*3)
	size := 0
	for i := 0; i < n; i++ {
		if s[i] == ' ' {
			bs[size] = '%'
			bs[size+1] = '2'
			bs[size+2] = '0'
			size += 3
		} else {
			bs[size] = s[i]
			size++
		}
	}
	return string(bs[:size])
}

func main() {

	s := "We are happy."
	result := replaceSpace(s)
	fmt.Println(result)
}
