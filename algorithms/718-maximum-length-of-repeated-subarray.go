package main

import "fmt"

func main() {
	fmt.Println(LCS("1AB2345CD","12345EF"))
	fmt.Println(LCS("abcdefg","hijklmn"))
}

func LCS(str1 string ,  str2 string) string {
	m, n := len(str1), len(str2)
	if m <= 0 || n <= 0 {
		return "-1"
	}

	dp := make([][]int, m)
	for k := 0; k < m; k++ {
		dp[k] = make([]int, n)
	}

	length, idx1 := 0, 0
	for i := 0; i < m; i++ {
		if str1[i] == str2[0] {
			dp[i][0] = 1
			length, idx1 = 1, i
		}
	}

	for j := 0; j < n; j++ {
		if str1[0] == str2[j] {
			dp[0][j] = 1
		}
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if str1[i] == str2[j] {
				dp[i][j] = dp[i - 1][j - 1] + 1
				if length < dp[i][j] {
					length = dp[i][j]
					idx1 = i
				}
			}
		}
	}

	if length > 0 {
		start, end := idx1 - length + 1, idx1 + 1
		return str1[start:end]
	} else {
		return "-1"
	}

}