class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window

        # left = 0, right = 0
        # store letters in set()
        # left++ -> dec window when we hit a dupe letter -> dec window until no dupes
            # while dupe in set:
                # left -> remove left from set -> left++
        # right++ -> inc window each time 
        # lenSubstring = right - left + 1


        left = 0
        right = 0
        maxLength = 0

        substringLetters = set()

        while right < len(s):
            while s[right] in substringLetters: # we found a dupe. remove letters until no dupes
                substringLetters.remove(s[left])
                left += 1

            substringLetters.add(s[right])
            maxLength = max(maxLength, right - left + 1) # calc curr substring len
            right += 1
        return maxLength

