from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            # Left sorted portion of the array
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            # Right sorted portion of the array
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
        return -1  # Return -1 if nothing found


class  Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) -1
        
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            
            #left sorted portion of the array
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            #right sorted portion of the array
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l  = mid + 1
                    
                    
    #else return -1 if nothing found
    
    
# Create an instance of the Solution class
solution = Solution()

# Test case: a rotated sorted array
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

# Call the search method
result = solution.search(nums, target)

# Check the result
if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print("Target not found in the array")
        