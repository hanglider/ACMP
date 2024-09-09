package main

import (
	"fmt"
	"os"
)

func main() {
	var k int16
	fmt.Fscan(os.Stdin, &k)
	fmt.Println((k*10+9)*10 + (9 - k))
}
