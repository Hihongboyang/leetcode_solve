#
# @lc app=leetcode.cn id=295 lang=python3
# @lcpr version=30204
#
# [295] 数据流的中位数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 优先队列, 堆

"""
刚开始的想法是使用一个小顶堆, 先弹出一半的元素(记录最后弹出的元素), 然后动态的将元素加入到堆中, 
每加入一个元素就弹出一个元素, 弹出的元素就是中间的值(或者与前一个值取平均获得). 
这个方法的问题是: 如果新加入的元素, 都比堆顶的元素还小, 一个堆没办法再回溯到前面弹出的元素.比如
先有  1 2 3 4 5 6 7, 弹出一半元素  1 2 3 | 4 5 6 7. 再不断的加入 1,然后弹出1.
1 2 3 1 1 | 1 4 5 6 7    在 1 1 1 1 2 3 4 5 6 7 中位数应该是 (2+3)/2. 一个堆时却是 (3+1)/2.
所以我们还是需要记住之前从堆中弹出的元素, 并且他们也是有序的.
"""
import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # 存储较小的一半元素（Python 的 heapq 默认是最小堆，所以用负数模拟最大堆）
        self.min_heap = []  # 存储较大的一半元素

    def addNum(self, num: int) -> None:
        # 先将元素插入 max_heap
        heapq.heappush(self.max_heap, -num)
        # 将 max_heap 的堆顶元素弹出并插入 min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        # 如果 min_heap 的大小大于 max_heap，调整平衡
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end



