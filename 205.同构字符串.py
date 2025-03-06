#
# @lc app=leetcode.cn id=205 lang=python3
# @lcpr version=30204
#
# [205] 同构字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t_map = dict()
        t_s_map = dict()
        for s_c, t_c in zip(s, t):
            if (s_t_map.get(s_c) and s_t_map[s_c] != t_c) or (
                t_s_map.get(t_c) and t_s_map[t_c] != s_c
            ):
                return False

            s_t_map[s_c] = t_c
            t_s_map[t_c] = s_c

        return True


# @lc code=end


#
# @lcpr case=start
# "egg"\n"add"\n
# @lcpr case=end

# @lcpr case=start
# "foo"\n"bar"\n
# @lcpr case=end

# @lcpr case=start
# "paper"\n"title"\n
# @lcpr case=end

# @lcpr case=start
# "pppp"\n"eeee"\n
# @lcpr case=end

# @lcpr case=start
# "price"\n"prize"\n
# @lcpr case=end

# @lcpr case=start
# "price!"\n"prize?"\n
# @lcpr case=end

#
