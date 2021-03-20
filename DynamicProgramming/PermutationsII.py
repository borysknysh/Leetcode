class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def recurse(nums, idx, res):
            if idx == len(nums):
                res.append(list(nums))
                return
            temp_hash = defaultdict(int)
            for i in range(idx, len(nums), 1):
                if nums[i] in temp_hash:
                    continue
                temp_hash[nums[i]] = 1
                nums[idx], nums[i] = nums[i], nums[idx]
                recurse(nums, idx+1, res)
                nums[idx], nums[i] = nums[i], nums[idx]
        
        res = []
        recurse(nums, 0, res)
        
        return res
