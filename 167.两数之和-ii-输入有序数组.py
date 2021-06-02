#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
# class Solution:
#     def num_index(self, list_, number_):
#         start = 0
#         end = len(list_) - 1
#         mid_target = number_ //2

#         while(start<end):
#             mid_ = (start + end) // 2

#             if list_[mid_] > mid_target:
#                 end = mid_ - 1
#             elif list_[mid_] < mid_target:
#                 start = mid_ + 1
#             else:
#                 return mid_

#         return mid_

#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         mid_num = target // 2

#         mid_index = self.num_index(numbers, target)
#         left_ = mid_index
#         right_ = mid_index

#         while(left_>=0 and right_< len(numbers)):
#             target_sum = numbers[left_] + numbers[right_]
#             if target_sum > target:
#                 left_ -= 1
            
#             elif target_sum < target:
#                 right_ += 1
#             else:
#                 if numbers[left_] == numbers[right_]:
#                     left_ -= 1
#                 else:
#                     return [left_+1, right_+1]
                
        
#         return [left_+1, right_+1]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1      
        while left < right:
            if numbers[left] + numbers[right] == target:                
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left = left + 1
            else:
                right = right - 1
# @lc code=end

