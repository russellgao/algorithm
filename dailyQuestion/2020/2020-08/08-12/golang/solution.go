package main

import (
	"fmt"
)

func exist(board [][]byte, word string) bool {
	m := len(board)
	if m == 0 {
		return false
	}
	n := len(board[0])
	var dfs func(i, j, k int) bool
	dfs = func(i, j, k int) bool {
		if (i < 0 || i >= m) || (j < 0 || j >= n) || board[i][j] != word[k] {
			return false
		}
		if k == len(word)-1 {
			return true
		}
		tmp := board[i][j]
		board[i][j] = '/'
		res := dfs(i+1, j, k+1) || dfs(i, j+1, k+1) || dfs(i-1, j, k+1) || dfs(i, j-1, k+1)
		board[i][j] = tmp
		return res
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if dfs(i, j, 0) {
				return true
			}
		}
	}
	return false
}

func main() {
	board := [][]byte{[]byte{'A', 'B', 'C', 'E'}, []byte{'S', 'F', 'C', 'S'}, []byte{'A', 'D', 'E', 'E'}}
	word := "ABCCED"
	result := exist(board, word)
	fmt.Println(result)
}
