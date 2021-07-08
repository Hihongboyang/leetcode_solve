/*
 * @lc app=leetcode.cn id=576 lang=c
 *
 * [576] 出界的路径数
 */

// @lc code=start

long mod = 10000000;
int N, m_, n_;

int findPaths(int m, int n, int maxMove, int startRow, int startColumn)
{

    N = maxMove;
    m_ = m;
    n_ = n;
    int f[m * n][N + 1];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == 0)
            {
                add(i, j, f);
            }
            if (i == m - 1)
            {
                add(i, j, f);
            }
            if (j == 0)
            {
                add(i, j, f);
            }
            if (j == n - 1)
            {
                add(i, j, f);
            }
        }
    }

    int dirs[][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    for (int step = 1; step <= N; step++)
    {
        for (int k = 0; k < m * n; k++)
        {
            int x = (*parseIdx(k)), y = (*(parseIdx(k)+1));
            for (int d = 0; d < 2; d++)
            {
                int nx = x + dirs[d][0], ny = y + dirs[d][1];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n)
                {
                    f[k][step] += f[getIndex(nx, ny)][step - 1];
                    f[k][step] %= mod;
                }
            }
        }
    }
    return f[getIndex(startRow, startColumn)][maxMove];
}

void add(int x, int y, int *f)
{
    int idx = getIndex(x, y);
    for (int step = 1; step <= N; step++)
    {
        (*(*(f+idx)+ step))++;
    }
}

int getIndex(int x, int y)
{
    return x * n_ + y;
}

int *parseIdx(int idx)
{
    int *p;
    int ret[] = {idx / n_, idx % n_};
    p = ret;
    return p;
}

// @lc code=end
