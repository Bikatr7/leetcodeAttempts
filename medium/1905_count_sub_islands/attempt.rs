/**
 * Kaden Bilyeu (Bikatr7)
 * 2024-08-27
 * 1905. Count Sub Islands (Medium)
 * 
 * Description:
 * You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
 * An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
 * Return the number of islands in grid2 that are considered sub-islands.
 * 
 * Example 1:
 * Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
 * Output: 3
 * Explanation: The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
 * 
 * Example 2:
 * Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
 * Output: 2 
 * Explanation: The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
 * 
 * Constraints:
 * m == grid1.length == grid2.length 
 * n == grid1[i].length == grid2[i].length
 * 1 <= m, n <= 500
 * grid1[i][j] and grid2[i][j] are either 0 or 1.
 * 
 * Topics: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
 * 
 * Hints:
 * 1. Let's use floodfill to iterate over the islands of the second grid
 * 2. Let's note that if all the cells in an island in the second grid if they are represented by land in the first grid then they are connected hence making that island a sub-island
 */

impl Solution 
{
    pub fn count_sub_islands(grid1: Vec<Vec<i32>>, mut grid2: Vec<Vec<i32>>) -> i32 
    {
        let m = grid1.len();
        let n = grid1[0].len();
        let mut count = 0;

        for i in 0..m 
        {
            for j in 0..n 
            {
                if grid2[i][j] == 1 && Self::dfs(&grid1, &mut grid2, i, j) 
                {
                    count += 1;
                }
            }
        }

        count
    }

    fn dfs(grid1: &Vec<Vec<i32>>, grid2: &mut Vec<Vec<i32>>, i: usize, j: usize) -> bool 
    {
        if i >= grid1.len() || j >= grid1[0].len() || grid2[i][j] == 0 
        {
            return true;
        }

        grid2[i][j] = 0; // Mark as visited
        let mut is_sub_island = grid1[i][j] == 1;

        let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        for (di, dj) in directions.iter() 
        {
            let ni = i  as i32 + di;
            let nj = j as i32 + dj;
            if ni >= 0 && nj >= 0 
            {
                is_sub_island &= Self::dfs(grid1, grid2, ni as usize, nj as usize);
            }
        }

        is_sub_island
    }
}