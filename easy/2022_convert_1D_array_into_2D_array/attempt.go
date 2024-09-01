// Kaden Bilyeu (Bikatr7)
// 2024-09-01
// 2022. Convert 1D Array Into 2D Array (Easy)

// Description:
// You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with m rows and n columns using all the elements from original.
// The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.
// Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.

// Example 1:
// Input: original = [1,2,3,4], m = 2, n = 2
// Output: [[1,2],[3,4]]

// Example 2:
// Input: original = [1,2,3], m = 1, n = 3
// Output: [[1,2,3]]

// Example 3:
// Input: original = [1,2], m = 1, n = 1
// Output: []

// Constraints:
// 1 <= original.length <= 5 * 10^4
// 1 <= original[i] <= 10^5
// 1 <= m, n <= 4 * 10^4

// Topics: Array, Matrix, Simulation

// Hints:

// Hint 1 : When is it possible to convert original into a 2D array and when is it impossible?
// Hint 2 : It is possible if and only if m * n == original.length
// Hint 3 : If it is possible to convert original to a 2D array, keep an index i such that original[i] is the next element to add to the 2D array.

package main

func construct2DArray(original []int, m int, n int) [][]int {
	if m*n != len(original) {
		return nil
	}

	result := make([][]int, m)
	for i := range result {
		result[i] = original[i*n : (i+1)*n]
	}

	return result
}
