package main

import (
	"fmt"
	"ProgrammingInGo/MinMovesToSeatEveryone"
)

func main() {
	// test the function
	// Use Exported Types to have visibility into functions from different package
	fmt.Println(MinMovesToSeatEveryone.MinMovesToSeat([]int{3,1,5}, []int{2,7,4}))
	fmt.Println(MinMovesToSeatEveryone.MinMovesToSeat([]int{4,1,5,9}, []int{1,3,2,6}))
	fmt.Println(MinMovesToSeatEveryone.MinMovesToSeat([]int{2,2,6,6}, []int{1,3,2,6}))
}