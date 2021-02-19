package main

func singleNumbers(nums []int) []int {
	ret := 0
	for _, num := range nums {
		ret ^= num
	}
	mask := 1
	for mask&ret == 0 {
		mask <<= 1
	}
	a, b := 0, 0
	for _, num := range nums {
		if num&mask == 0 {
			a ^= num
		} else {
			b ^= num
		}
	}
	return []int{a, b}
}

func main() {
	nums := []int{4, 1, 4, 6}
	result := singleNumbers(nums)
	print(result)
}
