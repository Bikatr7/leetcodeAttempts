// Kaden Bilyeu (Bikatr7)
// 2024-04-27
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

function lexicalOrder(n: number): number[] 
{
    const result: number[] = new Array(n);
    let current: number = 1;
    let index: number = 0;

    while (index < n)
    {
        result[index++] = current;
        if (current * 10 <= n)
        {
            current *= 10;
        }
        else
        {
            if (current >= n)
            {
                current = Math.floor(current / 10);
            }
            current++;
            while (current % 10 === 0)
            {
                current = Math.floor(current / 10);
            }
        }
    }

    return result;
}