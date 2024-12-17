#
# @lc app=leetcode.cn id=1343 lang=python3
# @lcpr version=30204
#
# [1343] 大小为 K 且平均值大于等于阈值的子数组数目
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        arr_len = len(arr)
        left = 0
        right = 0
        max_sum = 0
        count = 0

        while right < arr_len:
            max_sum += arr[right]
            if left + right + 1 >= k:
                if max_sum >= k * threshold:
                    count += 1
                max_sum -= arr[left]
                left += 1
            right += 1
        return count


# @lc code=end


#
# @lcpr case=start
# [2,2,2,2,5,5,5,8]\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# [11,13,17,23,29,31,7,5,2,3]\n3\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# [10,9,8,7,6,5]\n4\n7\n
# @lcpr case=end


# @lcpr case=start
#  [5,5,5,5,5]\n5\n5\n
# @lcpr case=end

# @lcpr case=start
#  [1,1,1,1,1]\n5\n1\n
# @lcpr case=end


#
