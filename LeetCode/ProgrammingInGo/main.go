package main

import (
	"fmt"
	"ProgrammingInGo/MinMovesToSeatEveryone"
	"ProgrammingInGo/MergeAlternately"
	"ProgrammingInGo/gcd"
	"ProgrammingInGo/KidsWithGreatestCandies"
	"ProgrammingInGo/ReverseWords"
	"ProgrammingInGo/productofelements"
)

func main() {
	// test the function
	// Use Exported Types to have visibility into functions from different package
	fmt.Println(MinMovesToSeatEveryone.MinMovesToSeat([]int{3,1,5}, []int{2,7,4}))
	fmt.Println(MinMovesToSeatEveryone.MinMovesToSeat([]int{4,1,5,9}, []int{1,3,2,6}))
	fmt.Println(MinMovesToSeatEveryone.MinMovesToSeat([]int{2,2,6,6}, []int{1,3,2,6}))

	// test the function
	fmt.Println(MergeAlternately.MergeAlternate("abc", "pqr"))
	fmt.Println(MergeAlternately.MergeAlternate("ab", "pqrs"))
	fmt.Println(MergeAlternately.MergeAlternate("abcd", "pq"))

	// test the function
	fmt.Println(gcd.GCDofStrings("ABCABC", "ABC"))
	fmt.Println(gcd.GCDofStrings("ABABAB", "ABAB"))
	fmt.Println(gcd.GCDofStrings("LEET", "CODE"))

	// test the function
	fmt.Println(KidsWithGreatestCandies.KidsWithCandies([]int{2,3,5,1,3}, 3))
	fmt.Println(KidsWithGreatestCandies.KidsWithCandies([]int{4,2,1,1,2}, 1))

	// test the function
	fmt.Println(ReverseWords.ReverseTokens("the sky is blue"))
	fmt.Println(ReverseWords.ReverseTokens("  hello world  "))
	fmt.Println(ReverseWords.ReverseTokens("a good   example"))

	// test the function
	fmt.Println(productofelements.ProductExceptSelf([]int{1,2,3,4}))
	fmt.Println(productofelements.ProductExceptSelf([]int{-1, 1, 0, -3, 3}))
}
