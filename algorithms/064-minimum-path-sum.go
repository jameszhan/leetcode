package main

import "fmt"

func main() {
	matrix := [][]int{
		{0, 1, 2, 3},
		{4, 5, 6, 7},
		{8, 9, 10, 11},
	}
	fmt.Println(minPathSum(matrix))
}

func minvalue(x int, y int) int {
	if x > y {
		return y
	} else {
		return x
	}
}

func minPathSum(matrix [][]int) int {
	m := len(matrix)
	n := len(matrix[0])
	dp := make([][]int, m)
	for k := 0; k < m; k++ {
		dp[k] = make([]int, n)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 && j == 0 {
				dp[i][j] = matrix[i][j]
			} else if i == 0 {
				dp[i][j] = matrix[i][j] + dp[i][j-1]
			} else if j == 0 {
				dp[i][j] = matrix[i][j] + dp[i-1][j]
			} else {
				dp[i][j] = matrix[i][j] + minvalue(dp[i-1][j], dp[i][j-1])
			}
		}
	}
	return dp[m-1][n-1]
}
