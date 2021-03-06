class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length_n = len(needle)
        length_hs = len(haystack)
        if needle == '':
            return 0

        for i in range(length_hs-length_n+1):
            if needle in haystack[i:i+length_n]:
                return i
            
        return -1 
