#
# @lc app=leetcode.cn id=136 lang=python3
# @lcpr version=30204
#
# [136] 只出现一次的数字
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

"""
异或运算⊕的三个性质:
1任何数和0做异或运算,结果仍然是原来的数,即 a⊕0=a
2数和其自身做异或运算,结果是 0, a⊕a=0
3异或运算满足交换率和结合律 a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b
这里就运用了第三个性质, a是成对出现的, b落单了,就将b挑选出来了
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        ret = 0
        for n in nums:
            ret ^= n
        
        return ret
        
# @lc code=end



#
# @lcpr case=start
# [2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,1,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

