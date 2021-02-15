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
	for i := 1; i < n -1; i++ {
	    h := min(lefts[i], rights[i])
	    if h > heights[i] {
	        ans += h - heights[i]
        }
    }

	return int64(ans)
}

//
//total, length = 0, len(heights)
//if length <= 2:
//    return 0
//max_left, max_right = [0 for _ in range(length)], [0 for _ in range(length)]
//# max_left[0] = heights[0]
//# max_right[length - 1] = heights[length - 1]
//
//for i in range(1, length):
//    max_left[i] = max(max_left[i - 1], heights[i - 1])
//for i in reversed(range(0, length - 1)):
//    max_right[i] = max(max_right[i + 1], heights[i + 1])
//
//for i in range(1, length - 1):
//    m = min(max_left[i], max_right[i])
//    if m > heights[i]:
//        total += (m - heights[i])
//
//return total
