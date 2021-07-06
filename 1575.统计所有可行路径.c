/*
 * @lc app=leetcode.cn id=1575 lang=c
 *
 * [1575] 统计所有可行路径
 */

// @lc code=start
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>

int *cache = NULL;

int mod = 1000000007;

int dfs(int *locations, int m, int n, int site, int finish, int fuel)
{
    if (cache[site * m + fuel] != -1)
    {
        return cache[site * m + fuel];
    }

    if (fuel == 0 && site != finish)
    {
        cache[site * m + fuel] = 0;
    }
    bool hasNext = false;

    for (int i = 0; i < n; i++)
    {
        if (i != site)
        {
            int need = abs(locations[site] - locations[i]);
            if (fuel >= need)
            {
                hasNext = true;
                break;
            }
        }
    }

    if (fuel != 0 && !hasNext)
    {
        int a = cache[site * m + fuel] = (site == finish ? 1 : 0);
        return a;
    }

    int sum = (site == finish ? 1 : 0);

    for (int i = 0; i < n; i++)
    {
        if (i != site)
        {
            int need = abs(locations[i] - locations[site]);
            if (fuel >= need)
            {
                sum += dfs(locations, m, n, i, finish, fuel - need);
                sum %= mod;
            }
        }
    }
    cache[site * m + finish] = sum;
    return sum;
}

int countRoutes(int *locations, int locationsSize, int start, int finish, int fuel)
{
    int m = locationsSize;

    cache = (int *)malloc(sizeof(int) * m * (fuel + 1));
    memset(cache, -1, sizeof(int) * m * (fuel + 1));

    return dfs(locations, m, locationsSize, start, finish, fuel);
}

// int main(int argc, char const *argv[])
// {
//     int some[] = {2,3,6,8,4};
//     int ret;
//     ret = countRoutes(&some, 5, 1, 3, 5);
//     printf("%d ", ret);
//     return 0;
// }

// @lc code=end
