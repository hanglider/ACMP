package main
 
import (
    "fmt"
)
 
func max(a, b int) int {
    if a < b {
        return b
    } 
    return a
}
 
func main() {
    var n int 
    fmt.Scan(&n)
    var a[] int 
    var x int
    for i := 0; i < n; i++ {
        fmt.Scan(&x)
        a = append(a, x)
    }
 
    var d[] int 
    for i := 0; i < n; i++ {
        d = append(d, 0)
    }
 
    for i := 0; i < n; i++ {
        d[i] = 1
        for j := 0; j < i; j++ {
            if (a[j] < a[i]) {
                d[i] = max(d[i], 1 + d[j])
			}
		}
	}

	var ans = d[0]
	for i := 0; i < n; i++ {
		ans = max(ans, d[i])
	}
	fmt.Print(ans)

}