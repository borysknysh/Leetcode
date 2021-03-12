class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        length = len(height)
        # cover edge case
        if length < 2:
            return 0
        left_max_arr = [height[0]] # initalize with first element
        right_max_arr = [height[-1]] # initializa with last element
        
        # for each element in the height list find maximum values to the left
        for i in range(1,length,1):
            left_max_arr.append(max(left_max_arr[-1], height[i]))
        # for each element in the height list find maximum values to the right
        for i in range(length-2,-1,-1):
            right_max_arr.append(max(right_max_arr[-1], height[i]))
        
        # iterate through the list and calculate for how many cells given element will be filled
        for i in range(length):
            ans += min(left_max_arr[i], right_max_arr[length-i-1]) - height[i]
        return ans
