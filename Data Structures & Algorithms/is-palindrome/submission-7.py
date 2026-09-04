class Solution:
    def isPalindrome(self, s: str) -> bool:
        # check front + back letter same -> 2 pointer
            # if same -> move both left/right
            # else -> return false
        # case insensitive -> convert each char to str.lower()
        # skip any non alphanumerics -> str.isalnum()() -> move left/right ptr

        left = 0
        right = len(s)-1

        while left < right:
            left_char = s[left]
            right_char = s[right]

            if left_char.isalnum() == False:
                left += 1
            elif right_char.isalnum() == False:
                right -= 1
            elif left_char.lower() == right_char.lower():
                left += 1
                right -= 1
            else:
                return False
        return True