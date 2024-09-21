// Kaden Bilyeu (Bikatr7)
// 2024-09-20
// 386. Lexicographical Numbers (Medium)

// Description:
// Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
// You must write an algorithm that runs in O(n) time and uses O(1) extra space.

// Example 1:
// Input: n = 13
// Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

// Example 2:
// Input: n = 2
// Output: [1,2]

// Constraints:
// 1 <= n <= 5 * 10^4

// Topics: Depth-First Search, Trie

// Hints:
// Hint 1: Consider using a depth-first search approach.
// Hint 2: Start with 1 and recursively explore its children (10, 11, 12, ...) before moving to 2.

package lexicographicalnumbers

func lexicalOrder(n int) []int {
	result := make([]int, 0, n)
	var dfs func(current int)

	dfs = func(current int) {
		if current > n {
			return
		}
		result = append(result, current)
		for ii := 0; ii < 10; ii++ {
			dfs(current*10 + ii)
		}
	}

	for ii := 1; ii < 10; ii++ {
		dfs(ii)
	}

	return result
}
