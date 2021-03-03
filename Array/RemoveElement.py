class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        acc_cntr = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != val:
                nums[acc_cntr] = nums[i]
                acc_cntr += 1
        return acc_cntr
