#
# @lc app=leetcode.cn id=321 lang=python3
# @lcpr version=30204
#
# [321] 拼接最大数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start

# 单调栈
# 先根据单调栈将单个列表中最大的数字选择出来, 然后将两个数组合并
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        return max(
            self.merge(self.pick_max(nums1, i), self.pick_max(nums2, k - i))
            for i in range(k + 1)
            if i <= len(nums1) and k - i <= len(nums2)
        )

    def merge(self, A, B):
        ret = []
        while A or B:
            bigger = A if A > B else B
            ret.append(bigger[0])
            bigger.pop(0)

        return ret

    def pick_max(self, nums, k):
        stack = []
        drop = len(nums) - k
        for num in nums:
            while drop and stack and stack[-1] < num:
                stack.pop()
                drop -= 1
            stack.append(num)

        return stack[:k]


# @lc code=end


#
# @lcpr case=start
# [3,4,6,5]\n[9,1,2,5,8,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [6,7]\n[6,0,4]\n5\n
# @lcpr case=end

# @lcpr case=start
# [3,9]\n[8,9]\n3\n
# @lcpr case=end

# @lcpr case=start
# [6,6,8]\n[5,0,9]\n3\n
# @lcpr case=end

#
