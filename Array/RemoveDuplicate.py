class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        cntr = 0
        
        while cntr < length-1:
            if nums[cntr] == nums[cntr+1]:
                del nums[cntr+1]
                cntr -= 1
                length -= 1
            cntr += 1
        return length
