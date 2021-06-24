/*
 * @lc app=leetcode.cn id=1289 lang=c
 *
 * [1289] 下降路径最小和  II
 */

// @lc code=start

int minFallingPathSum(int **arr, int arrSize, int *arrColSize)
{
    int m = arrSize, n = arrColSize[0];
    int f[m][n], val, i1 = -1, i2 = -1;

    for (int j = 0; j < n; j++)
    {
        val = arr[0][j];
        f[0][j] = val;

        if (val < (i1 == -1 ? INT_MAX : f[0][i1]))
        {
            i2 = i1;
            i1 = j;
        }
        else if (val < (i2 == -1 ? INT_MAX : f[0][i2]))
        {
            i2 = j;
        }
    }

    for (int i = 1; i < n; i++)
    {
        int ti1 = -1, ti2 = -1;
        for (int j = 0; j < n; j++)
        {
            f[i][j] = INT_MAX;
            int val = arr[i][j];

            if (j != i1)
            {
                f[i][j] = f[i - 1][i1] + val;
            }
            else
            {
                f[i][j] = f[i - 1][i2] + val;
            }

            if (f[i][j] < (ti1 == -1 ? INT_MAX : f[i][ti1]))
            {
                ti2 = ti1;
                ti1 = j;
            }
            else if (f[i][j] < (ti2 == -1 ? INT_MAX : f[i][ti2]))
            {
                ti2 = j;
            }
        }
        i1 = ti1;
        i2 = ti2;
    }
    int ans = INT_MAX;
    for (int i =0; i<n; i++)
    {
        ans = fmin(ans, f[n-1][i]);
    }
    return ans;
}
// @lc code=end
