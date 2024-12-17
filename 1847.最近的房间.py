#
# @lc app=leetcode.cn id=1847 lang=python3
# @lcpr version=30204
#
# [1847] 最近的房间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from sortedcontainers import SortedList
"""
思路
1. 先将rooms按照房间大小排序.
2. 对queries按照要求的房间min_size进行排序. 之后遍历序列
3. 每次取出一个queries, 遍历rooms, 将房间大小大于min_size的房间号都放入有序列表room_ids中.
4. 然后用二分法找到与preferred_id最相近的左右两个房间号
5. 最后比较两个房间号看, 哪个最为接近
"""

class Solution:
    def closestRoom(
        self, rooms: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        if len(queries) < 1:
            return []
        q_len = len(queries)
        r_len = len(rooms)
        room_ids = SortedList()
        rooms.sort(key=lambda x: x[1])  # 将room按照房间大小排序

        j = r_len - 1
        ans = [-1] * q_len
        for i in sorted(range(len(queries)), key=lambda i: -queries[i][1]):
            # 遍历queries数组
            preferred_id, min_size = queries[i]
            while j >= 0 and rooms[j][1] >= min_size:
                # 将size大于要求的room的id添加进入room_ids的有序列表
                room_ids.add(rooms[j][0])
                j -= 1

            diff = inf
            k = room_ids.bisect_left(preferred_id)  # 二分查找获得最左边的插入位置
            if k:
                diff = preferred_id - room_ids[k-1]  # 比较左边id的差值并记录
                ans[i] = room_ids[k-1]

            if k < len(room_ids) and room_ids[k] - preferred_id < diff:  # 计算右边的差值并于左边的差值比较
                ans[i] = room_ids[k]
        return ans



# @lc code=end


#
# @lcpr case=start
# [[2,2],[1,2],[3,2]]\n[[3,1],[3,3],[5,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[2,3],[3,5],[4,1],[5,2]]\n[[2,3],[2,4],[2,5]]\n
# @lcpr case=end

#
