package main

import "fmt"

func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}

func lcm(a, b int) int {
    return a * b / gcd(a, b)
}

func main() {
    var a, b int
    fmt.Scan(&a, &b)
    fmt.Println(lcm(a, b))
}