class Solution:
    def countAndSay(self, n: int) -> str:
        def countAndSayUtil(n):
            if n == 1:
                return '1'
            elif n == 2:
                return '11'
            else:
                s = countAndSayUtil(n-1)
                length = len(s)
                cntr = 1
                new_s = ''
                for i in range(0, length-1,1):
                    if s[i] == s[i+1]:
                        cntr += 1
                    else:
                        new_s = new_s + str(cntr)+s[i]
                        cntr = 1
                new_s = new_s + str(cntr)+s[-1]
                return new_s
            
        return countAndSayUtil(n)  
