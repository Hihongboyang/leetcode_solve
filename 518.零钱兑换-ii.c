/*
 * @lc app=leetcode.cn id=518 lang=c
 *
 * [518] 零钱兑换 II
 */

// @lc code=start
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int change(int amount, int *coins, int coinsSize)
{
    // 这是一个动态规划问题，这其中涉及两个循环，一个是：零钱相加的总和，需要从0开始一直到最终的目标。
    // 二是硬币的数组需要遍历， 相当于每个硬币的组合需要遍历。
    // 穷举分析： 假设求和为8的数， 2+2+2+2=8 2+3+3=8  4+4=8 2+2+4=8
    // 确定边界： 在没有硬币的时候，只有一种组合方式。我们只能找到下界。
    // 找到出规律： 这里的规律是：当要确定一个数值的硬币组合时，需要计算两种情况，
    // 1.不使用最新加入的硬币，就可以达到求和值。2.之前的求和值j再加上最新的硬币才能达到求和值i（j+coins）。
    // 写出状态转移方程：基于上面可以写出推倒公式，sum(k,i) = sum(k-1, i) + sum(k, i-coin) 其中k代表第几个硬币
    int dp[amount + 1];
    memset(dp, 0, sizeof(dp));
    dp[0] = 1;
    for (int i = 0; i < coinsSize; i++)
    {
        // 外面这层循环，以一个一个硬币开始。这一层就遍历了：在不加入新的硬币时，就累积到了要求的和值
        for (int j = coins[i]; j <= amount; j++)
        {
            // 这一层计算在加入新的硬币时，累积到和值的组合数
            dp[j] += dp[j - coins[i]];
        }
    }
    for (int i = 0; i < amount + 1; i++)
    {
        printf("%d ", dp[i]);
    }
    printf("\n");
    return dp[amount];
}

int main(int argc, char const *argv[])
{
    int coins[] = {1,4,9,16};

    change(12, &coins, 3);
    return 0;
}

// @lc code=end
