#
# @lc app=leetcode.cn id=703 lang=python3
# @lcpr version=30204
#
# [703] 数据流中的第 K 大元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 堆+优先队列
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._limit = k
        heapq.heapify(nums)
        for _ in range(len(nums) - self._limit):
            heapq.heappop(nums)
        self._queue = nums

    def add(self, val: int) -> int:
        heapq.heappush(self._queue, val)
        print(self._queue)
        for _ in range(len(self._queue) - self._limit):
            heapq.heappop(self._queue)
            
        return self._queue[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end



#
# @lcpr case=start
# ["KthLargest", "add", "add", "add", "add", "add"]\n[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]\n
# @lcpr case=end

# @lcpr case=start
# ["KthLargest", "add", "add", "add", "add"]\n[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]\n
# @lcpr case=end

# @lcpr case=start
# ["KthLargest","add","add","add","add","add"]\n[[1,[]],[-3],[-2],[-4],[0],[4]]\n
# @lcpr case=end

# @lcpr case=start
# ["KthLargest","add","add","add","add","add"]\n[[2,[0]],[-1],[1],[-2],[-4],[3]]\n
# @lcpr case=end

#

