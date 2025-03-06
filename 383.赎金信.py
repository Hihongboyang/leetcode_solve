#
# @lc app=leetcode.cn id=383 lang=python3
# @lcpr version=30204
#
# [383] 赎金信
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start'

# 哈希表
# 先统计magazine中每个字符的个数,
# 然后遍历ransomNote, 在字符个数表中查找, 
# 找到后计数个数减一, 如果找不到或者个数为0则返回False

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapping = Counter(magazine)

        for c in ransomNote:
            if mapping[c] > 0:
                mapping[c] -= 1
            else:
                return False
        return True
        
# @lc code=end



#
# @lcpr case=start
# "a"\n"b"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"ab"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"aab"\n
# @lcpr case=end

#

