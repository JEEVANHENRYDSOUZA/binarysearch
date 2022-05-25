#pivot element is the central element where i divide the array with one half in increasing and other half in decreasing order


class Solution(object):
    def pivotIndex(self, nums):
        start=0
        end=len(nums)-1
        while(start<end):
            middle=start+(end-start)//2
            if(nums[middle]>nums[0]):
                start=middle+1
            else:
                end=mid-1
                
        return start
