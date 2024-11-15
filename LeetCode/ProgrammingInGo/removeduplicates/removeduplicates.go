package removeduplicates

func RemoveDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	unique_index := 0
	for i := 1; i < len(nums); i++ {
		if nums[i] != nums[unique_index] {
			unique_index++
			nums[unique_index] = nums[i]
		}
	}
	return unique_index + 1
}
