package main

import "fmt"

func combinationPredict(a []int, k int) bool {
	for i := 0; i < k; i++ {
		if a[i] >= a[k] {
			return false
		}
	}
	return true
}

func combinationsDFS(a []int, n int, m int, k int, f func(arr []int)) {
	for i := 0; i < n; i++ {
		a[k] = i + 1
		if combinationPredict(a, k) {
			if k == m - 1 {
				f(a)
			} else {
				combinationsDFS(a, n, m, k + 1, f)
			}
		}
	}
}

func factorial(n int) int {
	ret := 1
	for i := 1; i <= n; i++ {
		ret *= i
	}
	return ret
}

func combineNumber(n int , m int) int {
	return factorial(n) / (factorial(m) * factorial(n - m))
}

func combine(n int, k int) [][]int {
	size := combineNumber(n, k)
	answers := make([][]int, size)
	a := make([]int, k)
	i := 0

	handle := func(arr []int) {
		candidate := make([]int, k)
		copy(candidate, arr)
		answers[i] = candidate
		i++
	}

	combinationsDFS(a, n, k, 0, handle)

	return answers
}

func main() {
	ret := combine(4, 2)
	fmt.Println(ret)
}


