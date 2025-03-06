#
# @lc app=leetcode.cn id=705 lang=python3
# @lcpr version=30204
#
# [705] 设计哈希集合
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 哈希表
class MyHashSet:
    def __init__(self):
        self.bukets = 1003
        self.mapping = [[] for _ in range(self.bukets)]

    def add(self, key: int) -> None:
        hash_key = key % self.bukets
        if key in self.mapping[hash_key]:
            return

        self.mapping[hash_key].append(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.bukets
        if key not in self.mapping[hash_key]:
            return

        self.mapping[hash_key].remove(key)

    def contains(self, key: int) -> bool:
        hash_key = key % self.bukets
        if key in self.mapping[hash_key]:
            return True

        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end


#
# @lcpr case=start
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"][[], [1], [2], [1], [3], [2], [2], [2], [2]]\n
# @lcpr case=end

#
