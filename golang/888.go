package golang

func fairCandySwap(aliceSizes []int, bobSizes []int) []int {
	var aliceSum int = 0
	var bobSum int = 0

	bobHashMap := map[int]struct{}{}

	for _, number := range aliceSizes {
		aliceSum += number
	}

	for _, number := range bobSizes {
		bobSum += number
		bobHashMap[number] = struct{}{}
	}

	targetDifference := (bobSum - aliceSum) / 2

	for _, number := range aliceSizes {
		_, ok := bobHashMap[number+targetDifference]

		if ok {
			return []int{number, number + targetDifference}
		}
	}

	return []int{0}
}
