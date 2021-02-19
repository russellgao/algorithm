package main

import "fmt"

func insertBits(N int, M int, i int, j int) int {
	N_j := N >> (j + 1) << (j + 1)
	N_i := (N >> i << i) ^ N
	N_i_j := N_i | N_j
	return N_i_j | (M << i)
}

func insertBits2(N int, M int, i int, j int) int {
	return (((N >> i << i) ^ N) | (N >> (j + 1) << (j + 1))) | (M << i)
}

func main() {
	a := 2
	b := 6
	c := insertBits2(1024, 19, a, b)
	fmt.Println(c)
}
