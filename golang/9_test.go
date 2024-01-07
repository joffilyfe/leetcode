package golang

import "testing"

func TestFirstIsPalindrome(t *testing.T) {
	input := 1221
	result := isPalindrome(input)

	if !result {
		t.Errorf(`isPalindrome(%v) = %v expected return %v`, input, result, true)
	}
}

func TestSecondIsPalindrome(t *testing.T) {
	input := -1221
	result := isPalindrome(input)

	if result {
		t.Errorf(`isPalindrome(%v) = %v expected return %v`, input, result, false)
	}
}

func TestThirdIsPalindrome(t *testing.T) {
	input := 10
	result := isPalindrome(input)

	if result {
		t.Errorf(`isPalindrome(%v) = %v expected return %v`, input, result, false)
	}
}
