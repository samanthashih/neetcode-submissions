class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 anagram exists in s2 -> true

        # sliding window s2: find window where has exact s1 letters count
        #                   l -> shrink l/restart window when r is not s1 letter 
        #                   r -> increment 
        # if {windowLetterCounts} = {s1LetterCounts} -> return true

        windowLetterCounts = defaultdict(int)
        s1LetterCounts = Counter(s1)
        print(s1LetterCounts)

        l = 0
        r = 0
        while r < len(s2):
            letter = s2[r]
            windowLetterCounts[letter] += 1
            
            while windowLetterCounts[letter] > s1LetterCounts[letter]:
                # s[r] letter does not belong in s1. restart window
                windowLetterCounts[s2[l]] -= 1
                l += 1

            if sum(windowLetterCounts.values()) == sum(s1LetterCounts.values()):
                print(s2[l:r+1])
                return True
            r += 1
        
        return False