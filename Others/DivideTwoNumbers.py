class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_min = -2147483648
        int_max = 2147483647
        
        has_flip_sign = False
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        elif dividend < 0:
            has_flip_sign = True
            dividend = -dividend
        elif divisor < 0:
            has_flip_sign = True
            divisor = -divisor
        
        summ = 0
        res = 0
        
        for k in range(31,-1,-1):
            if dividend >= summ + (divisor << k):
                summ += (divisor << k)
                res |= 1 << k
        
        corr = -res if has_flip_sign else res
        if corr > int_max:
            return int_max
        if corr < int_min:
            return int_min
        
        return -res if has_flip_sign else res
