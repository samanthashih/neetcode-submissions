class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Substring can have k other letters + 1 max letter (letter w/ max count)
        # len(substring) = k + maxLetterCount
        # sliding window l -> shrink while we exceed: k < len()-maxLetterCount. Update {letterCounts}
        #                r -> increment

        # Trick: we don't need to know what the actual maxLetter is, we just need 
        # the maxLetterCount. Every time we update {letterCounts}, check if we 
        # update maxLetterCount. When shrinking window, we don't need to update
        # maxLetterCount even though it'll prob be inaccurate bc we will keep a 
        # maxSubstring. We only update maxLetterCount when we find a new max in {letterCounts},
        # bc that will be the only chance for a better maxSubString, else 0% chance

        maxLetterCount = 0
        maxSubstring = 0
        letterCounts = defaultdict(lambda: 0)

        l = 0
        r = 0
        while r < len(s):
            letterCounts[s[r]] += 1
            maxLetterCount = max(maxLetterCount, letterCounts[s[r]])
            
            # check if substring exceeds k
            while k < (r-l+1) - maxLetterCount:
                letterCounts[s[l]] -= 1
                l += 1
            
            maxSubstring = max(maxSubstring, r-l+1)
            r += 1

        return maxSubstring