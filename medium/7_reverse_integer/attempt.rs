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

impl Solution
{
    pub fn reverse(mut x: i32) -> i32
    {
        let mut reversed = 0i32;
        
        while x != 0
        {
            match reversed.checked_mul(10).and_then(|r| r.checked_add(x % 10))
            {
                Some(r) => reversed = r,
                None => return 0,
            }
            x /= 10;
        }
        
        reversed
    }
}