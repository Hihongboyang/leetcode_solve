#
# @lc app=leetcode.cn id=220 lang=python3
# @lcpr version=30204
#
# [220] 存在重复元素 III
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff == 0:
            return False
        
        length = len(nums)
        left, right = 0, 0
        window = SortedList()

        while right < length:
            window.add(nums[right])
            if right - left > indexDiff:
                window.remove(nums[left])
                left += 1

            index = bisect.bisect_left(window, nums[right])

            if index > 0 and nums[right] - window[index - 1] <= valueDiff:
                return True
            if index < len(window) - 1 and window[index + 1] - nums[right] <= valueDiff:
                return True
            right += 1

        return False
        
# @lc code=end

#
# @lcpr case=start
# [1,2,3,1]\n3\n0\n
# @lcpr case=end

# @lcpr case=start
# [1,5,9,1,5,9]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1]\n1\n2\n
# @lcpr case=end

#

