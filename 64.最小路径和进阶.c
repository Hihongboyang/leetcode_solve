#include <stdio.h>
#include <limits.h>
#include <math.h>

int m, n;

int getIdx(int x, int y)
{
    return x * n + y;
}

int minPathSum(int **grid, int obstacleGridSize, int *obstacleGridColSize)
{
    // 题如64 题，此时如果要求在计算最小权值路径的基础上，输出权值最小的路径，怎么办？
    m = obstacleGridSize, n = obstacleGridColSize[0];
    int f[m][n];
    int g[m * n];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == 0 && j == 0)
            {
                f[i][j] = grid[i][j];
            }
            else
            {
                int top = i - 1 >= 0 ? f[i - 1][j] : INT_MAX;
                int left = j - 1 >= 0 ? f[i][j - 1] : INT_MAX;
                f[i][j] = fmin(top, left) + grid[i][j];
                // 使用公式 x*n+y 对路径进行编码。将路径存储起来
                g[getIdx(i, j)] = top < left ? getIdx(i - 1, j) : getIdx(i, j - 1); 
            }
        }
    }
    int idx = getIdx(m - 1, n - 1);

    int path[m + n][2];
    path[m + n - 1][0] = m - 1;
    path[m + n - 1][1] = n - 1;

    for (int i = 1; i < m + n; i++)
    {
        // 方向对g中存储的路径进行解码
        path[m + n - 1 - i][0] = idx / n;
        path[m + n - 1 - i][1] = idx % n;
        idx = g[idx];
    }

    for (int i = 0; i < m + n -1; i++)
    {
        // 输出路径
        int x = path[i][0], y = path[i][1];
        printf("(%d, %d) ", x,y);
    }
    printf("\n");

    return f[m - 1][n - 1];
}

int main(int argc, char const *argv[])
{
    int some[3][3] = {{1,3,1}, {1,5,1}, {4,2,1}};
    int *p[3];

    p[0] = some[0];
    p[1] = some[1];
    p[2] = some[2];

    int some2 = 3;
    printf("%d", minPathSum(p, 3, &some2));
    return 0;
}
