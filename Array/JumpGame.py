class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums)-1
        
        for pos in range(lastPos-1,-1,-1):
            if pos+nums[pos] >= lastPos:
                lastPos = pos
        return lastPos == 0
