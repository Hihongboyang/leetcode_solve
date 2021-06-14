/*
 * @lc app=leetcode.cn id=64 lang=c
 *
 * [64] 最小路径和
 */

// @lc code=start

int minPathSum(int **grid, int gridSize, int *gridColSize)
{
    int m = gridSize, n = *gridColSize;
    int f[m][n];
    f[0][0] = grid[0][0];

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i > 0 && j > 0)
            {
                f[i][j] = fmin(f[i - 1][j], f[i][j - 1]) + grid[i][j];
            }
            else if (i > 0)
            {
                f[i][j] = f[i - 1][j] + grid[i][j];
            }
            else if (j > 0)
            {
                f[i][j] = f[i][j - 1] + grid[i][j];
            }
        }
    }
    return f[m - 1][n - 1];
}
// @lc code=end
