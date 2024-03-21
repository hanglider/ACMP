package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	var sec []int
	var fi []int
	for i := 0; i < n; i++ {
		if a[i]%2 != 0 {
			fi = append(fi, a[i])
		} else {
			sec = append(sec, a[i])
		}
	}
	for i := 0; i < len(fi); i++ {
		fmt.Print(fi[i], " ")
	}
	fmt.Println()
	for i := 0; i < len(sec); i++ {
		fmt.Print(sec[i], " ")
	}
	fmt.Println()
	if len(fi) > len(sec) {
		fmt.Print("NO")
	} else {
		fmt.Print("YES")
	}
}
