package acmp
package main

import (
	"fmt"
)

func main() {
	var M, N int
	fmt.Scan(&M, &N)

	if M > N {
		M, N = N, M
	}

	limit := 1 << M
	dp := make([]int64, limit)

	for i := 0; i < limit; i++ {
		dp[i] = 1
	}

	for col := 1; col < N; col++ {
		nextDP := make([]int64, limit)
		for mask := 0; mask < limit; mask++ {
			for prev := 0; prev < limit; prev++ {
				if isValid(prev, mask, M) {
					nextDP[mask] += dp[prev]
				}
			}
		}
		dp = nextDP
	}

	var result int64
	for _, count := range dp {
		result += count
	}

	fmt.Println(result)
}

func isValid(prev, curr, M int) bool {
	for i := 0; i < M-1; i++ {
		b1 := (prev >> i) & 1
		b2 := (prev >> (i + 1)) & 1
		b3 := (curr >> i) & 1
		b4 := (curr >> (i + 1)) & 1

		if b1 == b2 && b2 == b3 && b3 == b4 {
			return false
		}
	}
	return true
}
