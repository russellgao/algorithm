package main

import (
	"fmt"
)

var parent []int = make([]int, 26)

func main() {
	equations := []string{"a==b", "b==c", "a==c", "d==c"}
	result := equationsPossible(equations)
	fmt.Println(result)

}

func equationsPossible(equations []string) bool {
	for i := 0; i < 26; i++ {
		parent[i] = i
	}
	for _, eq := range equations {
		if eq[1] == '=' {
			index1 := int(eq[0] - 'a')
			index2 := int(eq[3] - 'a')
			union(index1, index2)
		}

	}
	for _, eq := range equations {
		if eq[1] == '!' {
			index1 := int(eq[0] - 'a')
			index2 := int(eq[3] - 'a')
			if find(index1) == find(index2) {
				return false
			}
		}
	}

	return true
}

func find(index int) int {
	if index == parent[index] {
		return index
	}
	parent[index] = find(parent[index])
	return parent[index]
}

func union(index1, index2 int) {
	parent[find(index1)] = find(index2)
}
