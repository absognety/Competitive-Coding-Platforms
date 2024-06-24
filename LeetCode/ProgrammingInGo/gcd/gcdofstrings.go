// Leetcode 75

package gcd

func gcd_util(a int, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return a
}
func GCDofStrings(str1 string, str2 string) string {
	null_str := ""
	if (str1 + str2) != (str2 + str1) {
		return null_str
	}
	return str1[0:gcd_util(len(str1), len(str2))]
}