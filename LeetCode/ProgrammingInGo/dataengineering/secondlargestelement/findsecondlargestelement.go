package secondlargestelement

import (
	"math"
)

func FindSecondLargestElement(arr []int) any {
	const string1 = "No second largest element found"
	const string2 = "Array does not have enough elements"
	if len(arr) < 2 {
		return string2
	}
	var first int = math.MinInt64
	var second int = math.MinInt64
	for i := 0; i < len(arr); i++ {
		if arr[i] > first {
			second = first
			first = arr[i]
		} else if arr[i] > second && arr[i] != first {
			second = arr[i]
		}
	}
	if second == math.MinInt64 {
		return string1
	}
	return second
}
