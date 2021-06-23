/*
 * @lc app=leetcode.cn id=931 lang=c
 *
 * [931] 下降路径最小和
 */

// @lc code=start

int minFallingPathSum(int **matrix, int matrixSize, int *matrixColSize)
{
    int m = matrixSize, n = matrixColSize[0];
    int f[m][n], ans = INT_MAX;

    for (int i = 0; i < n; i++)
    {
        f[0][i] = matrix[0][i];
    }

    for (int i = 1; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (j == 0)
            {
                f[i][j] = fmin(f[i-1][j], f[i-1][j+1]);
            }
            else if (j == n-1)
            {
                f[i][j] = fmin(f[i-1][j-1], f[i-1][j]);
            }
            else
            {
                f[i][j] = fmin(fmin(f[i-1][j-1], f[i-1][j]), f[i-1][j+1]);
            }
            f[i][j] += matrix[i][j];
        }
    }

    for (int i=0; i<n; i++)
    {
        ans = fmin(ans, f[m-1][i]);
    }
    return ans;
}
// @lc code=end
