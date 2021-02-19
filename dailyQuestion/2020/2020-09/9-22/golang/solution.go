package main

import "fmt"

func main() {
	result := numJewelsInStones("aA", "aDAAADFAEAAaaa")
	fmt.Println(result)
}

func numJewelsInStones(J string, S string) int {
	mappings := map[byte]bool{}
	for i := 0; i < len(J); i++ {
		mappings[J[i]] = true
	}
	count := 0
	for j := 0; j < len(S); j++ {
		if mappings[S[j]] {
			count++
		}
	}
	return count
}
