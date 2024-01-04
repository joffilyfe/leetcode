package golang

import "testing"

func TestFirstGetDecimalValue(t *testing.T) {
	last := ListNode{Val: 1}
	middle := ListNode{Val: 0, Next: &last}
	head := ListNode{Val: 1, Next: &middle}

	result := getDecimalValue(&head)
	expected := 5

	if result != expected {
		t.Fatalf(`getDecimalValue(%v) = %v, expected: %v`, head, result, expected)
	}
}
