#
# @lc app=leetcode.cn id=128 lang=python3
# @lcpr version=30204
#
# [128] 最长连续序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 哈希表
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)  # 转换成集合
        ret = 0
        for n in nums:
            if n-1 in nums:
                # 如果 n-1 在集合中那就应该从n-1开始
                continue
            # n 是序列的起点
            y = n + 1  # 从n+1开始查找
            while y in nums: # 不断探索
                y += 1
            # 循环结束后，y-1 是最后一个在哈希集合中的数
            ret = max(ret, y - n)
        return ret
        
# @lc code=end



#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,2]\n
# @lcpr case=end

#

