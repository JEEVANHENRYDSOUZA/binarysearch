class Solution:
    def mySqrt(self, x) :
        if x == 1:
            return 1
        left = 0
        right = x
        while left <= right:
            mid = (left + right)//2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return trunc(right)
