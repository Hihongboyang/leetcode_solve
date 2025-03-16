#
# @lc app=leetcode.cn id=811 lang=python3
# @lcpr version=30204
#
# [811] 子域名访问计数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        if not cpdomains:
            return []

        times_dict = dict()
        for cpdomain in cpdomains:
            tiems, domain = cpdomain.split()
            tiems = int(tiems)

            domain_list = domain.split(".")
            for i in range(len(domain_list) - 1, -1, -1):
                sub_domain = ".".join(domain_list[i:])
                if sub_domain not in times_dict:
                    times_dict[sub_domain] = tiems
                else:
                    times_dict[sub_domain] += tiems

        res = []
        for key in times_dict.keys():
            res.append(str(times_dict[key]) + " " + key)
        return res


# @lc code=end


#
# @lcpr case=start
# ["9001 discuss.leetcode.com"]\n
# @lcpr case=end

# @lcpr case=start
# ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]\n
# @lcpr case=end

#
