#
# @lc app=leetcode.cn id=239 lang=python3
# @lcpr version=30204
#
# [239] 滑动窗口最大值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    # 在窗口中维护一个最大堆，堆顶元素就是最大值
    # 每次窗口移动，将新元素加入堆中，同时将超出窗口大小的最大的元素移除(需要知道值的索引, 所以存储值时要带上索引)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)

        heap  = [(-nums[i], i) for i in range(k)]  # python的heapq是最小堆，所以存储的时候取负值
        heapq.heapify(heap)

        ret = [-heap[0][0]]
        for i in range(k, length):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] <= i-k:
                heapq.heappop(heap)

            ret.append(-heap[0][0])

        return ret

        
# @lc code=end



#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

