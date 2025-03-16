#
# @lc app=leetcode.cn id=149 lang=python3
# @lcpr version=30204
#
# [149] 直线上最多的点数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 哈希表
# 利用斜率作为字典查询的键. 通过计算两个点之间的斜率判断是不是在一个直线上.
import math


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        if length < 3:
            return length

        ret = 0
        for i in range(length):
            line_dict = dict()
            line_dict[0] = 0
            same = 1
            for j in range(i + 1, length):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                # 使用最大公约数, 解决倍数问题n*k
                gcd_dx_dy = math.gcd(abs(dx), abs(dy))
                if (dx > 0 and dy > 0) or (dx < 0 and dy < 0):
                    dx = abs(dx) // gcd_dx_dy
                    dy = abs(dy) // gcd_dx_dy
                # 使y为负数
                elif dx < 0 and dy > 0:
                    dx = -dx // gcd_dx_dy
                    dy = -dy // gcd_dx_dy
                elif dx > 0 and dy < 0:
                    dx = dx // gcd_dx_dy
                    dy = dy // gcd_dx_dy
                elif dx == 0 and dy != 0:
                    # 水平线
                    dy = 1
                elif dx != 0 and dy == 0:
                    # 垂直线
                    dx = 1

                key = (dx, dy)  # "归一化dx,dy后作为字典的键"
                if key in line_dict:
                    line_dict[key] += 1
                else:
                    line_dict[key] = 1

            ret = max(ret, same + max(line_dict.values()))
        return ret


# @lc code=end


#
# @lcpr case=start
# [[1,1],[2,2],[3,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]\n
# @lcpr case=end

#
