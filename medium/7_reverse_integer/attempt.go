// Kaden Bilyeu (Bikatr7)
// 2024-03-14
// 7. Reverse Integer (Medium)

// Description:
// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

// Example 1:
// Input: x = 123
// Output: 321

// Example 2:
// Input: x = -123
// Output: -321

// Example 3:
// Input: x = 120
// Output: 21

// Constraints:
// -2^31 <= x <= 2^31 - 1

// Topics: Math

// Hints:
// Hint 1: Think about how to handle the sign of the integer.
// Hint 2: Be careful with overflow when reversing the integer.

package solution

import "math"

func reverse(x int) int {
	reversed := 0
	for x != 0 {
		pop := x % 10
		if (reversed > math.MaxInt32/10) || (reversed < math.MinInt32/10) ||
			(reversed == math.MaxInt32/10 && pop > 7) ||
			(reversed == math.MinInt32/10 && pop < -8) {
			return 0
		}
		reversed = reversed*10 + pop
		x /= 10
	}
	return reversed
}
