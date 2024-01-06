package golang

func binarySearch1539(arr []int, target int, size int) int {
	left, right := 0, size-1

	for left <= right {
		middle := (left + right) / 2

		if arr[middle] == target {
			return target
		} else if target > arr[middle] {
			left = middle + 1
		} else if target < arr[middle] {
			right = middle - 1
		}
	}

	return -1
}

func findKthPositive(arr []int, k int) int {

	count := 0
	size := len(arr)

	for i := 1; i <= arr[size-1]; i++ {
		result := binarySearch1539(arr, i, size)

		if result == -1 {
			count++

			if count == k {
				return i
			}
		}
	}

	return arr[size-1] + (k - count)
}
