class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l++ -> if we find dupe, (1) record maxLen (2) shrink window until get rid of dupe & dont forget to remove letters from set()
        # r++ -> 
        # Track dupes in set()

        if len(s) <= 1:
            return len(s)

        l = 0
        r = 1
        substringChars = set()
        maxLen = 0

        substringChars.add(s[l])
        while r < len(s):
            newChar = s[r]
            if newChar in substringChars:
                maxLen = max(maxLen, r-l)
                while newChar in substringChars:
                    # shrink window until s[r] not in set
                    substringChars.remove(s[l])
                    l += 1
            
            substringChars.add(s[r])
            r += 1
            
        return max(maxLen, len(substringChars))