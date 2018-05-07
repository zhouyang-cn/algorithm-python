# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/description/
class Solution:

    @staticmethod
    def remove_duplicates(nums):
        if len(nums) <= 1:
            return len(nums)
        index = 0
        for i in range(len(nums)):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]

        return index + 1


num_array = [0, 1, 1, 2, 2, 3, 3, 3, 4, 4]
length = Solution.remove_duplicates(num_array)
print("[ ", end="")
for num in range(length):
    print(num, end=" ")
print("]", "")
