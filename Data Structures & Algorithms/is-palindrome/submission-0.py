class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter string: only letters + numbers + lowercase
        filteredStr = ""
        for char in s:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
                filteredStr += char
        filteredStr = filteredStr.lower()
        print(filteredStr)

        # Two pointers: front & back of str
        # keep moving towards middle + compare char values
        # if str[front] != str[back] -> char values diff, not palindrome -> return false
        # else keep moving towards middle
        # once pointers cross -> palindrome

        front = 0 
        back = len(filteredStr) - 1

        while front < back:
            if filteredStr[front] != filteredStr[back]:
                return False
            else:
                front += 1
                back -= 1
        return True