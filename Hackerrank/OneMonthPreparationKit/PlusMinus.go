package main

import (
	"fmt"
)

/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

func plusMinus(arr []int32) {
	// Write your code here
	cnt_positive := 0
	cnt_negative := 0
	cnt_zeros := 0
	for _, item := range arr {
		if item > 0 {
			cnt_positive++
		} else if item < 0 {
			cnt_negative++
		} else {
			cnt_zeros++
		}
	}
	fmt.Printf("%.6f\n", float64(cnt_positive)/float64(len(arr)))
	fmt.Printf("%.6f\n", float64(cnt_negative)/float64(len(arr)))
	fmt.Printf("%.6f\n", float64(cnt_zeros)/float64(len(arr)))
}
