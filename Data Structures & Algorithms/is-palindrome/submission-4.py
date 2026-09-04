class Solution:
    def isPalindrome(self, s: str) -> bool:
        # compare str & reverseStr - O(n) n=len(s)
            # 1st clean str -> remove all non alphanumerics

        # 2 ptr on str: left, right - O(n)
        # move 2 pts inward & compare each char
            # don't need to clean str - just skip non alphanumerics

        left = 0
        right = len(s) - 1

        while left < right:
            left_char = s[left].lower()
            right_char = s[right].lower()

            if self.isAlphaNumeric(left_char) == False:
                left += 1
            elif self.isAlphaNumeric(right_char) == False:
                right -= 1
            elif left_char == right_char:
                left += 1
                right -= 1 
            else: 
                return False

        return True

    
    def isAlphaNumeric(self, char) -> bool:
        if (ord('a') <= ord(char) <= ord('z')) or (ord('0') <= ord(char) <= ord('9')):
            return True
        return False


# Test case
s = "race a car"
print(Solution().isPalindrome(s)) # False