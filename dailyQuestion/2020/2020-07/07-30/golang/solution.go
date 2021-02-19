package main

func findLongestSubarray(array []string) []string {
	if len(array) == 0 {
		return []string{}
	}
	dp := make([]int, len(array))
	if (array[0] >= "A" && array[0] <= "Z") || (array[0] >= "a" && array[0] <= "z") {
		dp[0] = -1
	} else {
		dp[0] = 1
	}
	for i := 1; i < len(array); i++ {
		if (array[i] >= "A" && array[i] <= "Z") || (array[i] >= "a" && array[i] <= "z") {
			dp[i] = dp[i-1] - 1
		} else {
			dp[i] = dp[i-1] + 1
		}
	}
	mappings := map[int]int{0: -1}
	for i := 0; i < len(dp); i++ {
		if _, ok := mappings[dp[i]]; !ok {
			mappings[dp[i]] = i
		}
	}
	maxLenth := 0
	left := 0
	right := 0
	for i := 0; i < len(dp); i++ {
		if i-mappings[dp[i]] > maxLenth {
			left = mappings[dp[i]]
			right = i + 1
			maxLenth = right - left
		}
	}
	if left >= right {
		return []string{}
	}
	return array[left+1 : right]
}

func main() {
	//nums := []string{"42", "10", "O", "t", "y", "p", "g", "B", "96", "H", "5", "v", "P", "52", "25", "96", "b", "L", "Y", "z", "d", "52", "3", "v", "71", "J", "A", "0", "v", "51", "E", "k", "H", "96", "21", "W", "59", "I", "V", "s", "59", "w", "X", "33", "29", "H", "32", "51", "f", "i", "58", "56", "66", "90", "F", "10", "93", "53", "85", "28", "78", "d", "67", "81", "T", "K", "S", "l", "L", "Z", "j", "5", "R", "b", "44", "R", "h", "B", "30", "63", "z", "75", "60", "m", "61", "a", "5", "S", "Z", "D", "2", "A", "W", "k", "84", "44", "96", "96", "y", "M"}
	nums := []string{"A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7", "H", "I", "J", "K", "L", "M"}
	result := findLongestSubarray(nums)
	print(result)
}
