package main

import "fmt"

func main() {
	var a [3]int32 
	for i := 0; i < 3; i++ {
		fmt.Scanf("%d", &a[i]) 
	}
	var min, max int32
	min = a[0]
	max = a[0]
	for _, value := range a {
		if value < min {
			min = value
		}
		if value > max {
			max = value
		}
	}
	fmt.Println(max - min)
}