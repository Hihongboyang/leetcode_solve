/*
 * @lc app=leetcode.cn id=70 lang=c
 *
 * [70] 爬楼梯
 */

// @lc code=start

int climbStairs(int n)
{
    long save_v[] = {1, 1}, result = 0;

    if (n == 0)
        return save_v[0];
    else if (n == 1)
        return save_v[1];

    for (int i = 1; i <= n; i++)
    {
        result = save_v[0] + save_v[1];
        save_v[0] = save_v[1];
        save_v[1] = result;
    }
    return save_v[0];
}
// @lc code=end
