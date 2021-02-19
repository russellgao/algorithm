package main

import (
	"fmt"
)

func main() {
	numCourses := 5
	prerequisites := [][]int{[]int{1, 0}, []int{2, 0}, []int{3, 0}, []int{4, 0},
		[]int{3, 2}, []int{4, 2}, []int{4, 3}, []int{3, 4}}
	result := canFinish(numCourses, prerequisites)
	fmt.Println(result)

}
func canFinish(numCourses int, prerequisites [][]int) bool {
	var (
		edges   = make([][]int, numCourses)
		visited = make([]int, numCourses)
		result  []int
		valid   = true
		dfs     func(u int)
	)

	dfs = func(u int) {
		visited[u] = 1
		for _, v := range edges[u] {
			if visited[v] == 0 {
				dfs(v)
				if !valid {
					return
				}
			} else if visited[v] == 1 {
				valid = false
				return
			}
		}
		visited[u] = 2
		result = append(result, u)
	}

	for _, info := range prerequisites {
		edges[info[1]] = append(edges[info[1]], info[0])
	}

	for i := 0; i < numCourses && valid; i++ {
		if visited[i] == 0 {
			dfs(i)
		}
	}
	return valid
}
