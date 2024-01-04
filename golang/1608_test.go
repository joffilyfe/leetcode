package golang

import "testing"

func TestSpecialArray(t *testing.T) {
	nums := []int{3, 5, 1}
	expected := 2
	result := specialArray(nums)

	if result != expected {
		t.Fatalf(`specialArray(%#v) = %v != %v`, nums, result, expected)
	}
}

func TestSecondSpecialArray(t *testing.T) {
	nums := []int{1, 4, 5}
	expected := 2
	result := specialArray(nums)

	if result != expected {
		t.Fatalf(`specialArray(%#v) = %v != %v`, nums, result, expected)
	}
}

func TestThirdSpecialArray(t *testing.T) {
	nums := []int{0, 1}
	expected := 1
	result := specialArray(nums)

	if result != expected {
		t.Fatalf(`specialArray(%#v) = %v != %v`, nums, result, expected)
	}
}

func TestFourthSpecialArray(t *testing.T) {
	nums := []int{0, 0}
	expected := -1
	result := specialArray(nums)

	if result != expected {
		t.Fatalf(`specialArray(%#v) = %v != %v`, nums, result, expected)
	}
}
