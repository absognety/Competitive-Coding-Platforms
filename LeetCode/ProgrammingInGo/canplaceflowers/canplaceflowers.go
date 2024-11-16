/*

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

*/

package canplaceflowers

func CanPlaceFlowers(flowerbed []int, n int) bool {
	fbed_length := len(flowerbed)
	var canPlant int = 0

	if fbed_length == 1 && flowerbed[0] == 0 && n == 1 {
		return true
	}

	if fbed_length > 1 && flowerbed[0] == 0 {
		if flowerbed[1] == 0 {
			flowerbed[0] = 1
			canPlant++
		}
	}

	for i := 1; i < fbed_length-1; i++ {
		if flowerbed[i-1] == 0 && flowerbed[i] == 0 && flowerbed[i+1] == 0 {
			flowerbed[i] = 1
			canPlant++
		}
	}

	if fbed_length > 1 && flowerbed[fbed_length-1] == 0 {
		if flowerbed[fbed_length-2] == 0 {
			flowerbed[fbed_length-2] = 1
			canPlant++
		}
	}

	return (canPlant >= n)
}
