package golang

import "testing"

func TestFirstCalculateTime(t *testing.T) {

	keyboard := "abcdefghijklmnopqrstuvwxyz"
	word := "cba"
	result := calculateTime(keyboard, word)
	expected := 4

	if result != expected {
		t.Errorf(`Expected %v but received %v`, expected, result)
	}
}
