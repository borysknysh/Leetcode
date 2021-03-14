class Solution:
    def searchRangeUtil(self, nums, target, l, r):
        if l > r:
            return -1
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.searchRangeUtil(nums, target, 0, mid-1)
        else:
            return self.searchRangeUtil(nums, target, mid+1, r)
            
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = self.searchRangeUtil(nums, target, 0, len(nums)-1)
        if res == -1:
            return [-1,-1]
        start = res
        end = res
        while start-1 >= 0 and nums[start-1] == target:
            start -= 1
        while end+1 < len(nums) and nums[end+1] == target:
            end += 1
        
        return start, end
