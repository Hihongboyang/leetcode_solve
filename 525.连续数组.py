#
# @lc app=leetcode.cn id=525 lang=python3
#
# [525] 连续数组
#

# @lc code=start

# 给定一个二进制数组 nums , 
# 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

# 使用前缀和来计算。和数为0和1数量的和，需要判断两个数字数量相等，
# 以-1 代表0，以1代表1，0和1向加，当和为0，说明俩数数量相同。
# 此题使用了这么一种思想： 因为是使用累积值来统计数组有多少0和1.
#  0, 0, 0,| 0, 1, 1, 0, 1, 0, 0, 1|, 0, 0, 0, 1
# -1,-2,-3,|-4,-3,-2,-3,-2,-3,-4,-3|,-4,-5,-6,-5
# 从上面的数组可以看到，当出现第一-3时，说明有3个0，当后面出现-3时说明
# 从开始到当前位置有配对数量的0和1 + 3个0，所以当去掉开头的3个0后，
# 剩下的就是配对数量0和1了。之后只要挑选出最长的子串就行了。
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mapping = {0: -1}
        sum_val = 0
        ret_max = 0
        for index,item in enumerate(nums):
            if item == 0:
                sum_val -= 1
            elif item == 1:
                sum_val += 1
            
            ret_ = mapping.setdefault(sum_val, index)
            ret_max = max(index-ret_, ret_max)
        
        return ret_max

# @lc code=end

