class Solution(object):
    def isPerfectSquare(self, num):
        start=1
        end=num
        while(start<=end):
            mid=start+(end-start)/2
            guessednumber=mid*mid
            if(guessednumber==num):
                return True
            elif(guessednumber<num):
                start=mid+1
            else:
                end=mid-1
        return False
       
