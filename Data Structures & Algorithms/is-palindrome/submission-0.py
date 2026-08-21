class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 # beginnning index for left pointer
        right = len(s) - 1 # index starts at 0 hence -1

        while left < right: # only care about comparisons when left < right
            while left < right and not s[left].isalnum():
                left += 1 # skip over non-alphanumeric chars if left ptr points at one
            while left < right and not s[right].isalnum():
                right -= 1 # do the same for right ptr
            if s[left].lower() != s[right].lower():
                return False # not palindrome if left & right do not equal
            
            left += 1
            right -= 1
            # move on to next chars
        return True
        