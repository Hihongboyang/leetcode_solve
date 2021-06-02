/*
 * @lc app=leetcode.cn id=217 lang=c
 *
 * [217] 存在重复元素
 */

// @lc code=start
#include <stdbool.h>

void qusort(int s[], int star, int end)
{
    // 快速排序算法
    int temp, low = star, heigh = end, middle;
    if (star < end)
    {
        middle = (star + heigh) / 2;
        temp = s[middle];
        s[middle] = s[low];
        while (low != heigh)
        {
            while (heigh > low && s[heigh] >= temp)
                --heigh;
            s[low] = s[heigh];
            while (heigh > low && s[low] <= temp)
                ++low;
            s[heigh] = s[low];
        }
        s[low] = temp;
        qusort(s, star, low - 1);
        qusort(s, low + 1, end);
    }
}

bool containsDuplicate(int *nums, int numsSize)
{
    int star = 0, end = numsSize - 1;
    qusort(nums, star, end);
    star = 1;
    while (star <= end)
    {
        if ((nums[star] - nums[star - 1]) == 0)
            return true;
        star += 1;
    }
    return false;
}
// @lc code=end
