#
# @lc app=leetcode.cn id=1296 lang=python3
# @lcpr version=30204
#
# [1296] 划分数组为连续数字的集合
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        mapping = collections.defaultdict(int)
        for n in nums:
            mapping[n] += 1

        for n in sorted(mapping.keys()):
            v = mapping[n]
            if v < 1:
                continue

            for i in range(k):
                mapping[n+i] -= v
                if mapping[n+i] < 0:
                    return False
        return True

        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,3,4,4,5,6]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,2,3,4,3,4,5,9,10,11]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n3\n
# @lcpr case=end

#

