package golang

/**
 * Definition for singly-linked list.
 * type ListNode2 struct {
 *     Val int
 *     Next *ListNode2
 * }
 */

type ListNode2 struct {
	Val  int
	Next *ListNode2
}

func addTwoNumbers(l1 *ListNode2, l2 *ListNode2) *ListNode2 {
	carry := 0
	head := &ListNode2{Val: 0}
	current := head

	for l1 != nil || l2 != nil || carry > 0 {
		total := carry

		if l1 != nil {
			total += l1.Val
			l1 = l1.Next
		}

		if l2 != nil {
			total += l2.Val
			l2 = l2.Next
		}

		carry = total / 10
		(*current).Next = &ListNode2{Val: total % 10}
		current = current.Next
	}

	return head.Next

}
