package golang

import "testing"
import "slices"

func TestOneFairCandySwap(t *testing.T) {
	aliceSizes := []int{1, 1}
	bobSizes := []int{2, 2}

	result := fairCandySwap(aliceSizes, bobSizes)
	expected := []int{1, 2}

	if !slices.Equal(result, expected) {
		t.Fatalf(`fairCandySwap({1, 2}, {2, 2}) = %v expected return %v`, result, expected)
	}
}

func TestTwoFairCandySwap(t *testing.T) {
	aliceSizes := []int{1, 2}
	bobSizes := []int{2, 3}

	result := fairCandySwap(aliceSizes, bobSizes)
	expected := []int{1, 2}

	if !slices.Equal(result, expected) {
		t.Fatalf(`fairCandySwap({1, 2}, {2, 3}) = %v expected return %v"`, result, expected)
	}
}
