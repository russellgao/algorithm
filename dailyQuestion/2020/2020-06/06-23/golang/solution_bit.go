package main

import (
	"fmt"
	"math/big"
)

func addBinary(a string, b string) string {
	ai, _ := new(big.Int).SetString(a, 2)
	bi, _ := new(big.Int).SetString(b, 2)
	ai.Add(ai, bi)
	return ai.Text(2)
}

func main() {
	a := "11"
	b := "1"
	result := addBinary(a, b)
	fmt.Println(result)
}
