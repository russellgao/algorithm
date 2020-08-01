package main

func missingNumber(nums []int) int {
	i, j := 0, len(nums)-1
	for i <= j {
		m := (i + j) >> 1
		if nums[m] == m {
			i = m + 1
		} else {
			j = m - 1
		}
	}
	return i
}

func main() {
	nums := []int{0, 1, 2, 3, 4, 5, 6, 7, 9}
	result := missingNumber(nums)
	print(result)
}
