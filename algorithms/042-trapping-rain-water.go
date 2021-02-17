package main

import "fmt"

func main() {
	a := []int{3, 1, 2, 5, 2, 4}
	fmt.Println(trap(a))
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func trap(heights []int) int64 {
	n := len(heights)
	lefts := make([]int, n)
	rights := make([]int, n)

	for i := 1; i < n; i++ {
		lefts[i] = max(lefts[i-1], heights[i-1])
	}

	for i := n - 2; i >= 0; i-- {
		rights[i] = max(rights[i+1], heights[i+1])
	}

	ans := 0
	for i := 1; i < n-1; i++ {
		h := min(lefts[i], rights[i])
		if h > heights[i] {
			ans += h - heights[i]
		}
	}

	return int64(ans)
}
