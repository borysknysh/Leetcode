class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        acc_cntr = 0
        length = len(nums)
        for i in range(1,length,1):
            if nums[acc_cntr] != nums[i]:
                acc_cntr += 1
                nums[acc_cntr] = nums[i]
        return acc_cntr+1
