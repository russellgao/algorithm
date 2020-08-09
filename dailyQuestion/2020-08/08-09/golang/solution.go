package main

import (
	"fmt"
	"strconv"
)

const (
	SIG_COUNT = 4
)

var (
	result   []string
	sigments []int
)

func restoreIpAddresses(s string) []string {
	result = []string{}
	sigments = make([]int, SIG_COUNT)
	dfs(s, 0, 0)
	return result
}

func dfs(s string, sigId, sigStart int) {
	if sigId == SIG_COUNT {
		if sigStart == len(s) {
			addr1 := ""
			for i := 0; i < SIG_COUNT; i++ {
				addr1 += strconv.Itoa(sigments[i])
				addr1 += "."
			}
			addr1 = addr1[:len(addr1)-1]
			result = append(result, addr1)
		}
		return
	}
	// 提前回溯
	if sigStart == len(s) {
		return
	}
	// 前导数字为0的情况
	if s[sigStart] == '0' {
		sigments[sigId] = 0
		dfs(s, sigId+1, sigStart+1)
	}
	addr := 0
	for sigEnd := sigStart; sigEnd < len(s); sigEnd++ {
		addr = addr*10 + int(s[sigEnd]-'0')
		if addr > 0 && addr <= 0xFF {
			sigments[sigId] = addr
			dfs(s, sigId+1, sigEnd+1)
		} else {
			break
		}
	}
}

func main() {
	s := "25525511135"
	result := restoreIpAddresses(s)
	fmt.Println(result)
}
