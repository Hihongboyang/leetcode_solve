#
# @lc app=leetcode.cn id=219 lang=python3
# @lcpr version=30204
#
# [219] 存在重复元素 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 滑动窗口+哈希表
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i, n in enumerate(nums):
            if i > k:
                window.remove(nums[i - k - 1])

            if n in window:
                return True
            else:
                window.add(n)
        return False


# @lc code=end


#
# @lcpr case=start
# [1,2,3,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,2,3]\n2\n
# @lcpr case=end

#
