#
# @lc app=leetcode.cn id=349 lang=python3
# @lcpr version=30204
#
# [349] 两个数组的交集
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 这个题目第一眼, 就想到将列表都变成集合, 然后两个集合求个交集即可, set(nums1) & set(nums2)
# 下边是每个数组只遍历一遍的方法

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        ret = []
        for n in nums2:
            if n in nums1:
                nums1.remove(n)
                ret.append(n)

        return ret
            
        
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n[2,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,5]\n[9,4,9,8,4]\n
# @lcpr case=end

#
