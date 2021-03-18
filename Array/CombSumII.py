class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def findNumbers(candidates, target, ans, temp, index, summ):
            if summ == target:
                ans.append(list(temp))
                return
            length = len(candidates)
            for i in range(index, length,1):
                if summ+candidates[i] > target:
                    continue
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                temp.append(candidates[i])
                findNumbers(candidates, target, ans, temp, i+1, summ+candidates[i])
                temp.pop()

        candidates = sorted(candidates)
        ans = []
        temp = []
        summ = 0
        findNumbers(candidates, target, ans, temp, 0, 0)
        
        return ans
