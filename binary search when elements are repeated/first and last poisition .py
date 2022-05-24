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
               # right=mid-1
                
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
