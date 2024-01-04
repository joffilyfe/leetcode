package golang

import "sort"

// binarySearch looks for the first element equal of immediate greater than target
func binarySearch(nums []int, target int) int {
	left, right := 0, len(nums)-1

	for left <= right {
		middle := (left + right) / 2

		if nums[middle] >= target {
			right = middle - 1
		} else {
			left = middle + 1
		}
	}

	return len(nums) - left
}

func specialArray(nums []int) int {

	sort.Ints(nums)

	for i := 1; i <= len(nums); i++ {
		if binarySearch(nums, i) == i {
			return i
		}
	}

	return -1
}
