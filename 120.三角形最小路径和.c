/*
 * @lc app=leetcode.cn id=120 lang=c
 *
 * [120] 三角形最小路径和
 */

// @lc code=start

// 此题还是先要将真实的数据结构写出来，才能观察到真正的规律
// 2
// 3 4
// 6 5 7
// 4 1 8 3

// 这里的条件是，
// 当j不等于0时，总是有左上节点的值可以继承
// 当j不等于最后一个元素时，总有上方节点的值可以继承
int minimumTotal(int **triangle, int triangleSize, int *triangleColSize)
{
    int m = triangleSize, n = triangleColSize[triangleSize-1], ans = INT_MAX;
    int f[m][n];
    f[0][0] = triangle[0][0];

    for (int i = 1; i < m; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            f[i][j] = INT_MAX;
            if (j != 0)
            {
                f[i][j] = fmin(f[i][j], f[i - 1][j - 1]);
            }
            if (j != i)
            {
                f[i][j] = fmin(f[i][j], f[i - 1][j]);
            }
            f[i][j] += triangle[i][j];
        }
    }
    for (int i=0; i<n; i++)
    {
        ans = fmin(ans, f[m-1][i]);
    }

    return ans;
}

// @lc code=end
