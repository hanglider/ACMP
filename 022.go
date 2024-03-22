package main

import (
	"fmt"
	"math/bits"
)

func main() {
	var n uint64
	fmt.Scan( &n)
	fmt.Print(bits.OnesCount64(n))
}
