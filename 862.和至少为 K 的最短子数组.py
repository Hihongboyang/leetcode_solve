#
# @lc app=leetcode.cn id=862 lang=python3
# @lcpr version=30204
#
# [862] 和至少为 K 的最短子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 单调栈+前缀和
from collections import deque
from itertools import accumulate


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = inf
        s = list(accumulate(nums, initial=0))  # 计算前缀和
        q = deque()
        for i, cur_s in enumerate(s):
            while q and cur_s - s[q[0]] >= k:
                ans = min(ans, i - q.popleft())
            while q and s[q[-1]] >= cur_s:
                q.pop()
            q.append(i)
        return ans if ans < inf else -1

# @lc code=end



#
# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n4\n
# @lcpr case=end

# @lcpr case=start
# [2,-1,2]\n3\n
# @lcpr case=end

#

