class Solution:
    def findMin(self, nums) -> int:
        left, right = 0, len(nums) - 1
    
        if nums[left] <= nums[right]:
            return nums[left]
        
        while left < right:
            mid = (left + right) // 2
          
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 
        
        return nums[left]

   
a= Solution()
num=[1]
print(a.findMin(num))

        