#our goal is to find the first and last position of the element in the array and then start printing it using a for loop
# once we get the element equal to the mid value then we nedd to search where the element present before it and the element present after it is the same or not
# if found same then we will have to store those index
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.findLeft(nums, target)
        right = self.findRight(nums, target)
        return [left, right]
    
    def findLeft(self, nums, target):
        idx = -1
        left = 0
        right = len(nums) - 1
            
        while (left <= right):
            mid = (left + right) // 2
            
            if nums[mid] == target:
                idx = mid
               # in normal binary search here we would have  exited the loop but since we are now searching two elements we would still continue the loop 
                
            if (nums[mid] >=target):
                right = mid - 1
            else:
                left = mid + 1
    
        return idx
    
    def findRight(self, nums, target):
        idx = -1
        left = 0
        right = len(nums) - 1
        
        while (left <= right):
            mid = (left + right) // 2
            
            if nums[mid] == target:
                idx = mid
                
                
            if (nums[mid] <= target):
                left = mid + 1
            else:
                right = mid - 1
    
        return idx
