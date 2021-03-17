class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        count_list = []
        for num in nums:
            count_list.append(sorted_nums.index(num))
        return count_list
