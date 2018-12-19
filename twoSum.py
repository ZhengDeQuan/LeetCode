nums = [3,3]
target = 6
def find(target, nums):
    if target < nums[0][0] or target > nums[-1][0]:
        return -1
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = int((l + r) / 2)
        if nums[mid][0] == target:
            return nums[mid][1]
        elif nums[mid][0] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def solve(target , nums):
    new_nums = [(num, i) for i, num in enumerate(nums)]

    new_nums = sorted(new_nums, key=lambda a: a[0])
    for iter,(a, i) in enumerate(new_nums):
        temp = new_nums.copy()
        temp.pop(iter)
        j = find(target - a, temp)
        if j >= 0:
            return [i, j]

if __name__ == "__main__":
    res = solve(target , nums)
    print(res)


# class Solution:
#
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#
#         def find(target, nums):
#             if target < nums[0][0] or target > nums[-1][0]:
#                 return -1
#             l, r = 0, len(nums) - 1
#             while l <= r:
#                 mid = int((l + r) / 2)
#                 if nums[mid][0] == target:
#                     return nums[mid][1]
#                 elif nums[mid][0] < target:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#             return -1
#
#         new_nums = [(num, i) for i, num in enumerate(nums)]
#         new_nums = sorted(new_nums, key=lambda a: a[0])
#         for iter, (a, i) in enumerate(new_nums):
#             temp = new_nums.copy()
#             temp.pop(iter)
#             j = find(target - a, temp)
#             if j >= 0:
#                 return [i, j]


