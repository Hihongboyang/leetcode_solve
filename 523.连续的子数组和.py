#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#

# @lc code=start

# 寻找子数组的核心有三点，1. 要使用前缀和，不断的将后面的数据加入到和中。2. 要找到一个条件将前面的数据去除掉。
# 3. 要用记录下相同条件下，元素的位置。
# 在525号那个题中，是一0和1的和为0为记录条件。在此题中，也要找到这种条件，
# 按照此题的要求，有当累加和除以k的余数相同时，满足这种条件。有下面的公式推倒 
# sum1 = （x*k）+余数  sum2 = (y*k) + 余数
# sum1 - sum2 = x*k - y*k = (x - y)*k
# 也就是当 sum2%k 的余数与 sum1%k 的余数相同时，sum2-sum1 就满足 n*k的条件。
# 那此时，只要记住每个余数和对应的位置，就可以找到子数组
# 23,2,4,6,7
#  5,1,5,5,0 余数
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mapping = {0: -1}
        _sum = 0
        for index, item in enumerate(nums):
            _sum += item
            before = mapping.setdefault(_sum % k, index)
            if index-before > 1:  # 之所以要大于1，是要满足数组至少要有两个的条件，为1的话就是前后两个相邻的数了。
                return True
            
        return False


# @lc code=end

