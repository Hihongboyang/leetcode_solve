/*
 * @lc app=leetcode.cn id=27 lang=c
 *
 * [27] 移除元素
 */

// @lc code=start

int removeElement(int *nums, int numsSize, int val)
{
    if (numsSize == 0) return 0;
    if (numsSize == 1)
    {
        if (nums[0] == val)
        {
            return 0;
        }
        else
        {
            return 1;
        }

    }

    int temp = nums[0], p = 0;

    for (int i = 1; i < numsSize; i++)
    {
        if (nums[i] != val)
        {
            nums[p++] = nums[i];
        }
    }
    if (temp != val)
    {
        nums[p++] = temp;
    }
    return p;
}
// @lc code=end
