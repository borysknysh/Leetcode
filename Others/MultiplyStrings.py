class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        length1 = len(num1)
        length2 = len(num2)
        
        result = [0]*(length1+length2)
        cntr1 = 0
        for i in range(length1-1, -1, -1):
            cntr2 = 0
            carry = 0
            for j in range(length2-1, -1, -1):
                summ = int(num1[i])*int(num2[j])+result[cntr1+cntr2]+carry
                carry = summ // 10
                result[cntr1+cntr2] = summ % 10
                cntr2 += 1
            if carry:
                result[cntr1+cntr2] += carry
            
            cntr1 += 1
        s = ''
        if result[-1] == 0:
            end = length1+length2-1
        else:
            end = length1+length2
        
        for i in range(end-1, -1, -1):
            s += str(result[i])
        return s
