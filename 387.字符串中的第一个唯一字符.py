#
# @lc app=leetcode.cn id=387 lang=python3
# @lcpr version=30204
#
# [387] 字符串中的第一个唯一字符
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapping = Counter(s)

        for i, c in enumerate(s):
            if mapping[c] == 1:
                return i
        return -1
        
# @lc code=end



#
# @lcpr case=start
# "leetcode"\n
# @lcpr case=end

# @lcpr case=start
# "loveleetcode"\n
# @lcpr case=end

# @lcpr case=start
# "aabb"\n
# @lcpr case=end

#

