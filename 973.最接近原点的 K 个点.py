#
# @lc app=leetcode.cn id=973 lang=python3
# @lcpr version=30204
#
# [973] 最接近原点的 K 个点
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:k]
# @lc code=end



#
# @lcpr case=start
# [[1,3],[-2,2]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[3,3],[5,-1],[-2,4]]\n2\n
# @lcpr case=end

#

