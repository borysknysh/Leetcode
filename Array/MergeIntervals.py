class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merged = [intervals[0]]
        for el in intervals[1:]:
            if merged[-1][1] < el[0]:
                merged.append(el)
            else:
                merged[-1][1] = max(merged[-1][1], el[1])
        
        return merged
