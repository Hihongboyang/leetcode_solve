/*
 * @lc app=leetcode.cn id=53 lang=c
 *
 * [53] 最大子序和
 */

// @lc code=start


int maxSubArray(int* nums, int numsSize){
    int pre = 0, maxAns = nums[0];
    for (int i = 0; i < numsSize; i++) {
        pre = fmax(pre + nums[i], nums[i]); // 累积值和当前值比较，取大的那个，
                                            // 当当前值大相当于重置了起始位置。
        maxAns = fmax(maxAns, pre);
    }
    return maxAns;
}
// @lc code=end

