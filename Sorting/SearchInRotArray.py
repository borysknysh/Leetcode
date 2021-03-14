class Solution:
    def searchUtil(self, nums, l, r, target):
        
        if l > r:
            return -1
        
        mid = (l+r) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[l] <= nums[mid]:
            if nums[l] <= target and nums[mid] >= target:
                return self.searchUtil(nums, l, mid-1, target)
            return self.searchUtil(nums, mid+1, r, target)
        
        if nums[mid] <= target and nums[r] >= target:
            return self.searchUtil(nums, mid+1, r, target)
        return self.searchUtil(nums, l, mid-1, target)
    
    def search(self, nums: List[int], target: int) -> int:
        return self.searchUtil(nums, 0, len(nums)-1, target)
