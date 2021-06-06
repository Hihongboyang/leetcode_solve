# 实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
class Solution:
    def isUnique(self, astr: str) -> bool:
        astr = sorted(list(astr))
        for i in range(1,len(astr)):
            if astr[i] == astr[i-1]:
                return False

        return True