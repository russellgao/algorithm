package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {
	a := []int{1, 2}
	b := []int{3, 4}
	c := findMedianSortedArrays(a, b)
	fmt.Println(c)
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	m := len(nums1)
	n := len(nums2)
	if n < m {
		m, n = n, m
		nums1, nums2 = nums2, nums1
	}
	imin := 0
	imax := m
	half_m_n := (m + n + 1) >> 1
	max_of_left := 0
	min_of_right := 0
	for imin <= imax {
		i := (imax + imin) >> 1
		j := half_m_n - i
		if i > 0 && nums1[i-1] > nums2[j] {
			imax = i - 1
		} else if i < m && nums1[i] < nums2[j-1] {
			imin = i + 1
		} else {
			if i == 0 {
				max_of_left = nums2[j-1]
			} else if j == 0 {
				max_of_left = nums1[i-1]
			} else {
				if nums1[i-1] > nums2[j-1] {
					max_of_left = nums1[i-1]
				} else {
					max_of_left = nums2[j-1]
				}
			}
			if (m+n)%2 == 1 {
				return float64(max_of_left)
			} else {
				if i == m {
					min_of_right = nums2[j]
				} else if j == n {
					min_of_right = nums1[i]
				} else {
					if nums1[i] < nums2[j] {
						min_of_right = nums1[i]
					} else {
						min_of_right = nums2[j]
					}
				}
				// 找到之后必须结束循环
				break
			}
		}
	}
	return float64(min_of_right+max_of_left) / 2
}
