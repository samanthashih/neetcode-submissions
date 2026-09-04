class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Substring can only have 1 letter which would be most freq letter (highest count)
        # numReplacements = len(substring) - mostFreqLetterCount -> store letterCounts
        # if numReplacements > k -> shrink substring l++ & update counts

        # Track mostFreqLetter -> maxHeap? Every r++, compare count[mostFreqLetter] < count[r] and update

        counts = defaultdict(int)
        l = 0
        r = 0 
        maxLen = 0
        # mostFreqLetter = s[0] don't need actual letter
        maxFreq = 0

        while r < len(s):
            counts[s[r]] += 1
            maxFreq = max(maxFreq, counts[s[r]])

            while (r-l+1 - maxFreq) > k:
                counts[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r-l+1)
            r += 1
        
        return maxLen