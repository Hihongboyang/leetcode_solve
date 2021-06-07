/*
 * @lc app=leetcode.cn id=494 lang=c
 *
 * [494] 目标和
 */

// @lc code=start
// 遍历所有的组合，统计所有满足条件的数量。
// 其中使用递归调用来代表一个“树”
int count;
int findTargetSumWays(int* nums, int numsSize, int target){
    count = 0;
    backtrack(nums, numsSize, target, 0, 0);
    return count;
}

void backtrack(int *nums, int numSize, int target, int index, int sum)
{
    if (index == numSize)
    {
        if (sum == target)
        {
            count ++;
        }
    }
    else
    {
        backtrack(nums, numSize, target, index+1, sum + nums[index]);
        backtrack(nums, numSize, target, index+1, sum - nums[index]);
    }
}
// @lc code=end

