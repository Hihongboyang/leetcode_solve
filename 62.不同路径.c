/*
 * @lc app=leetcode.cn id=62 lang=c
 *
 * [62] 不同路径
 */

// @lc code=start

int uniquePaths(int m, int n)
{
    int f[m][n];
    f[0][0] = 1;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i > 0 && j > 0)
            {
                f[i][j] = f[i - 1][j] + f[i][j - 1];
            }
            else if (i > 0)
            {
                f[i][j] = f[i - 1][j];
            }
            else if (j > 0)
            {
                f[i][j] = f[i][j - 1];
            }
        }
    }
    return f[m - 1][n - 1];
}
// @lc code=end
