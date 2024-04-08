package main

import (
	"fmt"
	"os"
	"math/big"
)

func main() {
	var a, b string
	fmt.Fscan(os.Stdin, &a)
	fmt.Fscan(os.Stdin, &b)
	var x, f1 = new(big.Int).SetString(a, 0)
	var y, f2 = new(big.Int).SetString(b, 0)
	if (f1 == true) && (f2 == true) {
		c := new(big.Int).Add(x, y)
		fmt.Println(c)
		os.Exit(0)
	}  

}