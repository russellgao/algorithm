package main

import "fmt"

func main() {
	digits := "234"
	result := letterCombinations(digits)
	fmt.Println(result)
}

var phoneMappings map[byte]string = map[byte]string{
	'2': "abc",
	'3': "def",
	'4': "ghi",
	'5': "jkl",
	'6': "mno",
	'7': "pqrs",
	'8': "tuv",
	'9': "wxyz",
}

var combindtions []string

func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}
	combindtions = []string{}
	backtrace(digits, 0, "")
	return combindtions
}

func backtrace(digits string, index int, combination string) {
	if index == len(digits) {
		combindtions = append(combindtions, combination)
	} else {
		digit := digits[index]
		letters := phoneMappings[digit]
		lettersCount := len(letters)
		for i := 0; i < lettersCount; i++ {
			backtrace(digits, index+1, combination+string(letters[i]))
		}
	}
}
