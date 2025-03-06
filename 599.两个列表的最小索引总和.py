#
# @lc app=leetcode.cn id=599 lang=python3
# @lcpr version=30204
#
# [599] 两个列表的最小索引总和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mapping = dict()
        ret = list()
        min_sum = len(list1) + len(list2)
        for i, l1 in enumerate(list1):
            mapping[l1] = i

        for i, l2 in enumerate(list2):
            if mapping.get(l2, None) is None:
                continue

            if (mapping[l2] + i) < min_sum:
                min_sum = mapping[l2] + i
                ret = [l2]
            elif mapping[l2] + i == min_sum:
                ret.append(l2)

        return ret


# @lc code=end


#
# @lcpr case=start
# ["Shogun", "Tapioca Express", "Burger King"\n["Piatti", "The Grill at Torrey Pines", "HungryHunter Steakhouse", "Shogun"]\n
# @lcpr case=end

# @lcpr case=start
# ["Shogun", "Tapioca Express", "Burger King"\n["KFC", "Shogun", "Burger King"]\n
# @lcpr case=end

#
