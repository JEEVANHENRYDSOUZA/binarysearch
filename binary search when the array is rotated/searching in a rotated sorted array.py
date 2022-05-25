#approach 1 would be to find the pivot element as the the array before and after the pivot element will be completely sorted once that is done that check on which side ot eh pivot element will the element lie
#approach 2 check wether the left side of middle or the right side which one is sorted and then eleminate the other half

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums)-1, target)
    
    
    
    def binary_search(self, nums, start, end, target):
        if start > end:
            return -1
        
        mid = (start+end)//2
        
        if nums[mid] == target:
            return mid
        
        
        # start to mid is sorted
        if nums[start] <= nums[mid]:
            if nums[start]<=target<nums[mid]:
                return self.binary_search(nums, start, mid-1, target)
            else:
                return self.binary_search(nums, mid+1, end, target)
        # mid to end is sorted
        else:
            if nums[mid]<target<=nums[end]:
                return self.binary_search(nums, mid+1, end, target)
            else:
                return self.binary_search(nums, start, mid-1, target)
