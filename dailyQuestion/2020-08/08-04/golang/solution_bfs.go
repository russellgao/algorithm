package main

import (
	"fmt"
)

func main() {
	numCourses := 5
	prerequisites := [][]int{[]int{1, 0}, []int{2, 0}, []int{3, 0}, []int{4, 0},
		[]int{3, 2}, []int{4, 2}, []int{4, 3}}
	result := canFinish(numCourses, prerequisites)
	fmt.Println(result)

}

func canFinish(numCourses int, prerequisites [][]int) bool {
	var (
		edges  = make([][]int, numCourses)
		indeg  = make([]int, numCourses)
		result []int
	)

	for _, info := range prerequisites {
		edges[info[1]] = append(edges[info[1]], info[0])
		indeg[info[0]]++
	}

	q := []int{}
	for i := 0; i < numCourses; i++ {
		if indeg[i] == 0 {
			q = append(q, i)
		}
	}

	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		result = append(result, u)
		for _, v := range edges[u] {
			indeg[v]--
			if indeg[v] == 0 {
				q = append(q, v)
			}
		}
	}
	return len(result) == numCourses
}
