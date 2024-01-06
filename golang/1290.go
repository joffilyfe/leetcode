package golang

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func getDecimalValue(head *ListNode) int {
	result := 0

	for head != nil {
		// shift bits to right
		result = result << 1
		// do a bitwise or operation
		// 100 | 001 -> b101 -> 5
		result = result | head.Val
		head = head.Next
	}

	return result
}
