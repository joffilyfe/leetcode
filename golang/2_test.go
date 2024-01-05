package golang

import "testing"
import "slices"

func TestFirstAddTwoNumbers(t *testing.T) {

	l1 := &ListNode2{
		Val: 2,
		Next: &ListNode2{
			Val:  4,
			Next: &ListNode2{Val: 3},
		},
	}
	l2 := &ListNode2{
		Val: 5,
		Next: &ListNode2{
			Val:  6,
			Next: &ListNode2{Val: 4},
		},
	}

	result := addTwoNumbers(l1, l2)
	s := []int{}

	for result != nil {
		s = append(s, result.Val)
		result = result.Next
	}

	expected := []int{7, 0, 8}

	if !slices.Equal(expected, s) {
		t.Fatalf(`Expected %v but received %v`, expected, s)
	}
}
