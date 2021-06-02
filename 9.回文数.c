/*
 * @lc app=leetcode.cn id=9 lang=c
 *
 * [9] 回文数
 */

// @lc code=start

bool isPalindrome(int x)
{
    int temp=0;
    if (x < 0 || (x != 0 && x % 10 == 0))
    {
        return false;
    }

    while(temp < x)
    {
        temp = (x % 10) + temp * 10;
        x = x / 10;
    }

    return x == temp || x == temp / 10;
}
// @lc code=end
