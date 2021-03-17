class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        #seats = [1,0,0,0]
        pos = 0
        maxDist = -1
        
        start = 0
        isStarted = False
        
        for seat in seats:
            if seat and isStarted == True: 
                maxDist = max((pos-start) // 2, maxDist)
                start = pos
            elif seat and isStarted == False:
                maxDist = max(pos-start, maxDist)
                isStarted = True
                start = pos
            elif not seat and pos == len(seats)-1:
                maxDist = max(pos-start, maxDist)
            pos += 1
        
        return maxDist
