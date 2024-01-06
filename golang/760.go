package golang

func anagramMappings(nums1 []int, nums2 []int) (ans []int) {
	m := make(map[int]int)

	for i, n := range nums2 {
		m[n] = i
	}

	for i := 0; i < len(nums1); i++ {
		ans = append(ans, m[nums1[i]])
	}

	return
}
