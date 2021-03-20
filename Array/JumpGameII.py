class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = [i for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(1,nums[i]+1):
                if i + j < len(nums):
                    steps[i+j] = min(steps[i+j], steps[i]+1)
        
        return steps[-1]
