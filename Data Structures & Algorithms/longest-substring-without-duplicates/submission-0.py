class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # iterate thru str, track maxLength
        # if next char not dupe -> right++
        # else if dupe -> left = s[dupe's index]
            # for each letter btwn i=left - dupe's index, del letterIndex[i]

        # how to check dupe?
        # store each encountered letter's index in hashmap

        maxLength = 0
        letterIndex = defaultdict()

        left = 0
        right = 0
        while right < len(s):
            letter = s[right]

            if letter in letterIndex:
                dupeIndex = letterIndex[letter]
                for i in range(left, letterIndex[letter]+1):
                    del letterIndex[s[i]]
                left = dupeIndex+1
                
            letterIndex[letter] = right
            
            maxLength = max(maxLength, right-left+1)

            right += 1
        
        return maxLength

# test case
        # "zx yzaxyz"
        # maxLength = 1
        # letterIndex
        # z : 0


                