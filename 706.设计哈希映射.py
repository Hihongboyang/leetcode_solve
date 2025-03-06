#
# @lc app=leetcode.cn id=706 lang=python3
# @lcpr version=30204
#
# [706] 设计哈希映射
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 哈希表
class MyHashMap:
    def __init__(self):
        self.bukets = 1003
        self.mapping = [[] for _ in range(self.bukets)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.bukets
        for item in self.mapping[hash_key]:
            if item[0] == key:
                item[1] = value
                return

        self.mapping[hash_key].append([key, value])

    def get(self, key: int) -> int:
        hash_key = key % self.bukets
        for item in self.mapping[hash_key]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        hash_key = key % self.bukets
        for i, item in enumerate(self.mapping[hash_key]):
            if item[0] == key:
                self.mapping[hash_key].pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end


#
# @lcpr case=start
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"][[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]\n
# @lcpr case=end

#
