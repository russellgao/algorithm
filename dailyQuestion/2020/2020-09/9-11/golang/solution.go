package main

import "fmt"

func main() {
	result := partition("aab")
	fmt.Println(result)
}
func partition(s string) (result [][]string) {
	temp := []string{}
	n := len(s)
	var check func(i, j int) bool
	check = func(i, j int) bool {
		for i <= j {
			if s[i] != s[j] {
				return false
			}
			i++
			j--
		}
		return true
	}

	var dfs func(idx int)
	dfs = func(idx int) {
		if idx == n {
			comb := make([]string, len(temp))
			copy(comb, temp)
			result = append(result, comb)
			return
		}
		for i := idx; i < n; i++ {
			if !check(idx, i) {
				continue
			}
			temp = append(temp, s[idx:i+1])
			dfs(i + 1)
			temp = temp[:len(temp)-1]
		}
	}
	dfs(0)
	return
}
