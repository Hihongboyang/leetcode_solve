#
# @lc app=leetcode.cn id=218 lang=python3
# @lcpr version=30204
#
# [218] 天际线问题
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 优先队列+堆

"""
预处理: 将每个建筑物的左右边界及其对应的高度信息提取出来,左边界对应的高度为负值,
       右边界对应的高度为正值,方便后续区分左右边界.
排序: 将所有边界点按照横坐标从小到大排序,如果横坐标相同,
      则按照高度从大到小排序（左边界）或从小到大排序（右边界）.
扫描: 遍历排序后的边界点,使用最大堆来维护当前扫描线位置的最大高度.
      当遇到左边界时,将其高度加入最大堆。
      当遇到右边界时,将对应的高度从最大堆中移除.
记录关键点: 在每次处理边界点后,检查当前最大堆的最大高度是否发生变化,如果发生变化,则记录该点为关键点.
"""
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for left, right, height in buildings:
            points.append((left, -height))
            points.append((right, height))

        points.sort()
        max_heap = [0]
        prev_max = 0
        ret = []
        for index, height in points:
            if height < 0:
                heapq.heappush(max_heap, height)
            else:
                max_heap.remove(-height)
                heapq.heapify(max_heap)

            if prev_max != -max_heap[0]:
                ret.append([index, -max_heap[0]])
                prev_max = -max_heap[0]

        return ret


# @lc code=end


#
# @lcpr case=start
# [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,2,3],[2,5,3]]\n
# @lcpr case=end

#
