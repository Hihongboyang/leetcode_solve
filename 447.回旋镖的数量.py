#
# @lc app=leetcode.cn id=447 lang=python3
# @lcpr version=30204
#
# [447] 回旋镖的数量
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 用hash表存储计算出的一个点到其他点的欧式距离, 然后再计算相等的距离的数量.
# 从这 m 个点中选择两个不同的点作为 j 和 k，共有 m × (m-1) 种方式。这是因为：
# 第一个点 j 有 m 种选择。
# 第二个点 k 有 m-1 种选择（不能与 j 重复）。
# 由于 j 和 k 的顺序不同会被视为不同的三元组，因此需要用排列而非组合。
from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        length = len(points)
        ret = 0
        for i in range(length):
            dist_mapping = defaultdict(int)

            for j in range(length):
                if i == j:
                    continue
                res = (points[i][0] - points[j][0]) ** 2 + (
                    points[i][1] - points[j][1]
                ) ** 2
                dist_mapping[res] += 1

            for value in dist_mapping.values():
                ret += value * (value - 1)
        return ret


# @lc code=end


#
# @lcpr case=start
# [[0,0],[1,0],[2,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[2,2],[3,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1]]\n
# @lcpr case=end

#
