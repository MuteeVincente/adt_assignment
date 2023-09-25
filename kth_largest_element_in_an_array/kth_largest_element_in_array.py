from typing import List

class Solution:
    def findkthLargest(self, nums: List[int] , k:int) -> int:
        k = len(nums) -k 
        
        def quickSelect(l, r):
            pivot, p = nums[r], l
            
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                    
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k:
                return quickSelect(l , p -1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]
            
        return quickSelect(0 , len(nums) - 1)
    
    
    
# Create an instance of the Solution class
solution = Solution()

# Test case: an array and k value
nums = [3,2,3,1,2,4,5,5,6]
k = 4

# Call the findkthLargest method
result = solution.findkthLargest(nums, k)

# Check the result
print(f"The {k}th largest element is: {result}")
