func longestValidParentheses(s string) int {
	n := len(s)
	result := 0
	if n == 0 {
		return result
	}
	left, right := 0, 0
	for i := 0; i < n; i++ {
		if s[i] == '(' {
			left++
		} else {
			right++
		}
		if left == right {
			result = max(result, left+right)
		} else if right > left {
			left, right = 0, 0
		}
	}
	left, right = 0, 0
	for i := n - 1; i >= 0; i-- {
		if s[i] == '(' {
			left++
		} else {
			right++
		}
		if left == right {
			result = max(result, left+right)
		} else if left > right {
			left, right = 0, 0
		}
	}
	return result
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}