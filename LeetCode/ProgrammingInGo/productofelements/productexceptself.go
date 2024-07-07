package productofelements
func computeProduct(arr []int) int {
    res := 1
    for i := 0; i < len(arr); i++ {
        res = res * arr[i]
    }
    return res
}

func ProductExceptSelf(nums []int) []int {
    result := []int{}
    for i := 0; i < len(nums); i++ {
        temp := []int{}
        temp = append(temp, nums[:i]...)
        temp = append(temp, nums[i+1:]...)
        result = append(result, computeProduct(temp))
    }
    return result
}