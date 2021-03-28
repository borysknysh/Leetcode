class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        inserted = False
        merged = []
        
        for i in range(len(intervals)):
            if not inserted:
                if newInterval[0] > intervals[i][1]:
                    merged.append(intervals[i])
                elif newInterval[1] < intervals[i][0]:
                    merged.append(newInterval)
                    merged.append(intervals[i])
                    inserted = True
                else:
                    start = min(intervals[i][0], newInterval[0])
                    end = max(intervals[i][1], newInterval[1])
                    merged.append([start, end])
                    inserted = True
            else:
                if merged[-1][1] < intervals[i][0]:
                    merged.append(intervals[i])
                else:
                    merged[-1][1] = max(merged[-1][1], intervals[i][1])
        if not inserted:
            merged.append(newInterval)
            
        return merged
