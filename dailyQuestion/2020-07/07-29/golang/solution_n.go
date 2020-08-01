package main

func missingNumber(nums []int) int {
	for i,v := range(nums) {
		if i != v {
			return i
		}
	}
	return len(nums)
}

func main() {
	nums := []int{0, 1, 2, 3, 4, 5, 6, 7, 9}
	result := missingNumber(nums)
	print(result)
}
