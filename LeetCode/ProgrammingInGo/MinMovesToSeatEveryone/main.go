package main

import (
	"fmt"
	"sort"
	"math"
)

func minMovesToSeat(seats []int, students []int) int {
	// sort both arrays
	sort.Ints(seats)
	sort.Ints(students)

	// count moves
	var moves int
	moves = 0
	for i := 0; i < len(seats); i++ {
		if (seats[i] != students[i]) {
			moves += int(math.Abs(float64(seats[i] - students[i])))
		}
	}
	return moves
}

func main() {
	// test the function
	fmt.Println(minMovesToSeat([]int{3,1,5}, []int{2,7,4}))
	fmt.Println(minMovesToSeat([]int{4,1,5,9}, []int{1,3,2,6}))
	fmt.Println(minMovesToSeat([]int{2,2,6,6}, []int{1,3,2,6}))
}