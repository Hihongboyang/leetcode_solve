#
# @lc app=leetcode.cn id=862 lang=python3
# @lcpr version=30204
#
# [862] 和至少为 K 的最短子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 滑动窗口
# 本题数组里的元素可能是负数，而滑动窗口算法适用于数组元素全是非负数的情况。
# 在元素全是非负的数组中，当把窗口的右边界往右移动时，窗口内元素的总和会单调递增；
# 当把左边界往右移动时，窗口内元素的总和会单调递减。
# 基于这种单调性，可以通过左右边界的移动动态调整窗口大小，从而满足条件。
# 然而，一旦数组中存在负数，窗口内元素总和就不再具有单调性。
# 比如，当窗口内元素总和大于等于 k 时，将左边界往右移，可能因为减去一个负数，
# 让窗口内元素总和变得更大，这样就无法借助滑动窗口的特性正确找出最短子数组。
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        left = right = 0
        limit = len(nums)
        sum_num = 0
        ret = inf
        
        while left <= right and right < limit:
            sum_num += nums[right]
            while sum_num >= k:
                sum_num -= nums[left]
                ret = min(ret, right - left + 1)
                left += 1
            right += 1
        return ret if ret < inf else -1
                
            
            
            
            
        
# @lc code=end


#
# @lcpr case=start
# [84,-37,32,40,95]\n167\n
# @lcpr case=end
# 单调性被破坏, 无法使用滑动窗口求解求解

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n4\n
# @lcpr case=end

# @lcpr case=start
# [2,-1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 3, 4, 5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [1, -1, 5, -2, 3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0, 0, 0, 1, 0, 0, 2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 3, 4, 5]\n15\n
# @lcpr case=end

# @lcpr case=start
# [1, -1, 1, -1, 1]\n2\n
# @lcpr case=end

#

