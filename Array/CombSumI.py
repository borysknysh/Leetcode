class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def findNumbers(candidates, summ, target, res, temp, index):
            if summ == target:
                res.append(list(temp))
                return
            length = len(candidates)
            for i in range(index, length,1):
                if summ + candidates[i] > target:
                    continue
                temp.append(candidates[i])
                findNumbers(candidates, summ+candidates[i], target, res, temp, i)
                temp.pop()
            
        candidates = sorted(candidates)
        res = []
        temp = []
        index = 0
        findNumbers(candidates, 0, target, res, temp, index)
        
        return res
