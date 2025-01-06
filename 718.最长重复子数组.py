#
# @lc app=leetcode.cn id=718 lang=python3
# @lcpr version=30204
#
# [718] 最长重复子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        length1, length2 = len(nums1), len(nums2)
        ret = 0

        for i in range(length1):
            ret = max(ret, self.findmaxlength(nums1, nums2, i, 0))

        for i in range(length2):
            ret = max(ret, self.findmaxlength(nums1, nums2, 0, i))

        return ret

    def findmaxlength(self, nums1, nums2, i, j):
        length1, length2 = len(nums1), len(nums2)
        max_length = 0
        cur_length = 0

        while i < length1 and j < length2:
            if nums1[i] == nums2[j]:
                cur_length += 1
                max_length = max(max_length, cur_length)
            else:
                cur_length = 0
            i += 1
            j += 1
        return max_length

        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,2,1]\n[3,2,1,4,7]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,0,0]\n[0,0,0,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1,1,1]\n[1,0,1,0,1]\n
# @lcpr case=end



#

