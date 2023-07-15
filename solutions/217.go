package main

import "fmt"

func containsDuplicate(nums []int) bool {
	seen := map[int]bool{}

	for _, num := range nums {
		if _, ok := seen[num]; ok {
			return true
		} else {
			seen[num] = true
		}
	}

	return false
}

func main() {
	fmt.Println(containsDuplicate([]int{1, 2, 3, 1}))
}
