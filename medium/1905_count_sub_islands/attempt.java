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

 class Solution
 {
     private int m, n;
     private int[][] grid1, grid2;
     private final int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
 
     public int countSubIslands(int[][] grid1, int[][] grid2)
     {
         this.m = grid1.length;
         this.n = grid1[0].length;
         this.grid1 = grid1;
         this.grid2 = grid2;
         
         // Pre-process: eliminate islands in grid2 that can't be sub-islands
         for (int i = 0; i < m; i++)
         {
             for (int j = 0; j < n; j++)
             {
                 if (grid2[i][j] == 1 && grid1[i][j] == 0)
                 {
                     dfs(i, j);
                 }
             }
         }
         
         int count = 0;
         for (int i = 0; i < m; i++)
         {
             for (int j = 0; j < n; j++)
             {
                 if (grid2[i][j] == 1)
                 {
                     dfs(i, j);
                     count++;
                 }
             }
         }
         
         return count;
     }
     
     private void dfs(int i, int j)
     {
         if (i < 0 || i >= m || j < 0 || j >= n || grid2[i][j] == 0)
         {
             return;
         }
         
         grid2[i][j] = 0;  // visited
         
         for (int[] dir : directions)
         {
             dfs(i + dir[0], j + dir[1]);
         }
     }
 }