#
# @lc app=leetcode.cn id=451 lang=python3
# @lcpr version=30204
#
# [451] 根据字符出现频率排序
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = defaultdict(int)
        ret = ""
        for c in s:
            # 对字符的计数加 1
            char_count[c] += 1
        char_count = [(-n, c) for c, n in char_count.items()]
        heapq.heapify(char_count)
        while char_count:
            one_item = heapq.heappop(char_count)
            ret += one_item[1] * -one_item[0]
        return ret

        
# @lc code=end



#
# @lcpr case=start
# "tree"\n
# @lcpr case=end

# @lcpr case=start
# "cccaaa"\n
# @lcpr case=end

# @lcpr case=start
# "Aabb"\n
# @lcpr case=end

#

