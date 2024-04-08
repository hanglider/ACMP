package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	var a = 0
	var b = 1
	for i := 0; i < n; i++ {
		a = a + b
		b = a - b
	}
	fmt.Print(a)

}