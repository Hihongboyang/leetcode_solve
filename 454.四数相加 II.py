#
# @lc app=leetcode.cn id=454 lang=python3
# @lcpr version=30204
#
# [454] 四数相加 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        mapping = defaultdict(int)

        for num1 in nums1:
            for num2 in nums2:
                sum_num = num1 + num2
                mapping[sum_num] += 1

        count = 0
        for num3 in nums3:
            for num4 in nums4:
                sum_num = -(num3 + num4)
                if sum_num in mapping:
                    count += mapping[sum_num]
        return count

# @lc code=end


#
# @lcpr case=start
# [1,2]\n[-2,-1]\n[-1,2]\n[0,2]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n[0]\n[0]\n
# @lcpr case=end

#
