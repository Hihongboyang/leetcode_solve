#
# @lc app=leetcode.cn id=1941 lang=python3
# @lcpr version=30204
#
# [1941] 检查是否所有字符出现次数相同
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 哈希表
from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)  # 计数
        return all(v == count[s[0]] for v in count.values())  # 判断是否都一样


# @lc code=end


#
# @lcpr case=start
# "abacbc"\n
# @lcpr case=end

# @lcpr case=start
# "aaabb"\n
# @lcpr case=end

#
