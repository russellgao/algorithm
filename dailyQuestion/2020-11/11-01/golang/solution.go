package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "catsanddog"
	wordDict := []string{"cat", "cats", "and", "sand", "dog"}
	result := wordBreak(s, wordDict)
	fmt.Println(result)
}

func wordBreak(s string, wordDict []string) (sentences []string) {
	wordmap := map[string]bool{}
	for _, word := range wordDict {
		wordmap[word] = true
	}
	n := len(s)
	dp := make([][][]string, n)

	var backtrace func(index int) [][]string
	backtrace = func(index int) [][]string {
		if dp[index] != nil {
			return dp[index]
		}
		wordList := [][]string{}
		for i := index + 1; i < n; i++ {
			word := s[index:i]
			if _, ok := wordmap[word]; ok {
				for _, nexttrace := range backtrace(i) {
					wordList = append(wordList, append([]string{word}, nexttrace...))
				}
			}
		}
		word := s[index:]
		if _, ok := wordmap[word]; ok {
			wordList = append(wordList, []string{word})
		}
		dp[index] = wordList
		return wordList
	}

	for _, item := range backtrace(0) {
		sentences = append(sentences, strings.Join(item, " "))
	}
	return
}
