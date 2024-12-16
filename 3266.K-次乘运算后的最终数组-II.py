#
# @lc app=leetcode.cn id=3266 lang=python3
# @lcpr version=30204
#
# [3266] K 次乘运算后的最终数组 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:  # 数组不变
            return nums

        MOD = 1_000_000_007
        n = len(nums)
        mx = max(nums)
        h = [(x, i) for i, x in enumerate(nums)]
        heapify(h)

        # 模拟，直到堆顶是 mx
        while k and h[0][0] < mx:
            x, i = h[0]
            heapreplace(h, (x * multiplier, i))
            k -= 1

        # 剩余的操作可以直接用公式计算
        h.sort()
        for i, (x, j) in enumerate(h):
            nums[j] = x * pow(multiplier, k // n + (i < k % n), MOD) % MOD
        return nums


# @lc code=end


#
# @lcpr case=start
# [2,1,3,5,6]\n5\n2\n
# @lcpr case=end

# @lcpr case=start
# [100000,2000]\n2\n1000000\n
# @lcpr case=end

#
