class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(s, o, c):
            if c == n:
                ans.append(s)
                return 
            else:
                if o < n:
                    generate(s+"(", o+1, c)
                if o > c:
                    generate(s+")", o, c+1)
        ans = []
        generate("", 0, 0)
        return ans
