class Solution:
    def judgeSquareSum(self, c) :
        def binary_search(start,end,num):
            mid = (start+end)//2
            if start > end:
                return False
            if (mid*mid) == num:
                return True
            elif (mid*mid) > num:
                return binary_search(start, mid-1, num)
            elif (mid*mid) < num:
                return binary_search(mid+1, end, num)
        a = 0
        while (a*a) <= c:
            b = c - int(a*a)
            if binary_search(0,b,b):
                return True
            a += 1
        return False
