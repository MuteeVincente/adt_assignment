from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            curSum = numbers[l] + numbers[r]
            
            if curSum > target:
                r -= 1
                
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        return []


# Create an instance of the Solution class
solution = Solution()

# Test case: a sorted array and a target value
numbers = [2, 7, 11, 15]
target = 9

# Call the twoSum method
result = solution.twoSum(numbers, target)

# Check the result
if result:
    print(f"Indices of the two numbers that add up to {target}: {result[0]}, {result[1]}")
else:
    print("No solution found.")
