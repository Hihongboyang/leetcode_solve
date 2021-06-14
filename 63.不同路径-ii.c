/*
 * @lc app=leetcode.cn id=63 lang=c
 *
 * [63] 不同路径 II
 */

// @lc code=start

int uniquePathsWithObstacles(int **obstacleGrid, int obstacleGridSize, int *obstacleGridColSize)
{
    
    int m = obstacleGridSize, n = obstacleGridColSize[0];
    int f[m][n];
    f[0][0] = obstacleGrid[0][0] == 1 ? 0 : 1;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (obstacleGrid[i][j] != 1)
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
            else
            {
                f[i][j] = 0;
            }
        }
    }
    return f[m - 1][n - 1];
}
// int main(int argc, char const *argv[])
// {
//     int some[2][2] = {{0,0},{0,0}};
//     int * p[2];

//     p[0] = some[0];
//     p[1] = some[1];

//     int some2 = 2;
//     printf("%d", uniquePathsWithObstacles(p, 2, &some2));
//     return 0;
// }

// @lc code=end
