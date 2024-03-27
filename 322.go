package main

import (
	"fmt"
)

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	var n int
	fmt.Scan(&n)
	t := make([]int, n+1)
	for i := 0; i < len(t); i++ {
		t[i] = 1e5
	}
	t[0] = 0
	var x int
	for j := 0; j < n; j++ {
		var a []int
		for i := 0; i < n-j; i++ {
			fmt.Scan(&x)
			a = append(a, x)
		}
		for i := 0; i < len(a); i++ {
			var f = i + j + 1
			t[f] = min(t[f], a[i]+t[j])
		}
	}
	fmt.Print(t[n])
}