/*
 * @lc app=leetcode.cn id=279 lang=c
 *
 * [279] 完全平方数
 */

// @lc code=start

/*
*给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于n。
*你需要让组成和的完全平方数的个数最少。给你一个整数n，返回和为n的完全平方数的 最少数量 。
*/
#include <limits.h>
#include <stdlib.h>

int numSquares(int n)
{
    // 此题和518的零钱兑换比较像，如果将1，4，9等想象成对应的硬币，就和518有相似的思路。
    // 不过此题中要求，数字组合中 数字个数 最少的组合中的 数字个数。
    // 按照动态规划的步骤，先穷举一下
    // 0 1 2 3 4 5 6 7 8 9 10 11 12
    // 0 1 2 3 1 2 3 4 2 1  2  3  3
    // 确定边界： 以0作为边界，组成他的平方数为0
    // 规律： 和518比较像的是，当加入一个不大于当前i的“硬币（平方数）”加入时，
    //       之前的累积值+新的硬币正好等于i。 即 dp[i - coin] + 1, 加1是因为，
    //       此时是引入了一个新硬币，所以要加一。同时要找到所有组合最小的数。
    //       因此有 minval = min(minval, f[i - coin]), f[i] = minval.
    int f[n + 1];
    f[0] = 0;
    for (int i = 1; i <= n; i++)
    {
        int minn = INT_MAX;
        for (int j = 1; j * j <= i; j++)
        {
            minn = fmin(minn, f[i - j * j]);
        }
        f[i] = minn + 1;
    }
    return f[n];
}
// @lc code=end
