package main

import (
	"fmt"
	"os"
)

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	var n int
	fmt.Fscan(os.Stdin, &n)
	if n == 0 {
		fmt.Println(1)
		os.Exit(0)
	}
	t := 1
	for i := 2; i <= Abs(n); i++ {
		t += i
	}
	if n <= 0 {
		fmt.Println(t*(-1) + 1)
	} else {
		fmt.Println(t)
	}

}
