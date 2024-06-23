package main

import (
	"fmt"
	"ProgrammingInGo/MinMovesToSeatEveryone"
	"ProgrammingInGo/MergeAlternately"
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
}