class Solution:
    def Palindrome(self, s:str) -> bool:
        newStr = ""
        
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        # -> [::-1] is the syntax for reversing a string in python
        return newStr == newStr[::-1]
    

# Create an instance of the Solution class
solution = Solution()

# Test case: a string to check for palindrome
s = "A man, a plan, a canal, Panama"

# Call the Palindrome method
result = solution.Palindrome(s)

# Check the result
if result:
    print(f"'{s}' is a palindrome.")
else:
    print(f"'{s}' is not a palindrome.")
