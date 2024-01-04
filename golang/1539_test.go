package golang

import "testing"

func TestFirstFindKthPositive(t *testing.T) {
	arr := []int{2,3,4,7,11}
	k := 5

	result := findKthPositive(arr, k)
	expected := 9

	if result != expected {
		t.Fatalf("findKthPositive(%v, %v) = %v but expected %v", arr, k, result, expected)
	}
}

func TestSecondFindKthPositive(t *testing.T) {
	arr := []int{1,2,3,4}
	k := 2

	result := findKthPositive(arr, k)
	expected := 6

	if result != expected {
		t.Fatalf("findKthPositive(%v, %v) = %v but expected %v", arr, k, result, expected)
	}
}
