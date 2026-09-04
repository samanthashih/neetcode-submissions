class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l++ -> if we find dupe, (1) record maxLen (2) shrink window until get rid of dupe & dont forget to remove letters from set()
        # r++ -> 
        # Track dupes in set()

        l = 0
        r = 0
        substringChars = set()
        maxLen = 0

        while r < len(s):
            while s[r] in substringChars:
                # shrink window until s[r] not in set
                substringChars.remove(s[l])
                l += 1
            
            substringChars.add(s[r])
            maxLen = max(maxLen, r-l+1)
            r += 1
            
        return maxLen