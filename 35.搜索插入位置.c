/*
 * @lc app=leetcode.cn id=35 lang=c
 *
 * [35] 搜索插入位置
 */

// @lc code=start

int searchInsert(int *nums, int numsSize, int target)
{
    int i;
    if (target > nums[numsSize - 1])
        return numsSize;
    if (target < nums[0])
        return 0;

    for(i=0; i<numsSize; i++)
    {
        if (nums[i] >= target) break;
    }
    return i;
}
// @lc code=end
