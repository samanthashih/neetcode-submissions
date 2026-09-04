class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 anagram is in s2 -> s1 letterCounts is in s2
        # if s1Letters == s2WindowLetters -> we found a window that is an s1 anagram

        # sliding window s2 to find substring that is an anagram of s1 
        #   -> we alr know what the substring window size = len(s1)
        #       we can have a fixed window size, check if anagram, shift if not anagram.
        # sliding window l -> l++ shrink window when r is not in s1 anagram.
        #                r -> r++

        s1Letters = Counter(s1)
        # s2WindowLetters = defaultdict(int)

        l = 0
        r = len(s1)-1
        s2WindowLetters = Counter(s2[l:r+1])
        
        while r < len(s2):
            if l != 0:
                s2WindowLetters[s2[r]] += 1

            # check if s2Window is s1 anagram

            if s1Letters == s2WindowLetters:
                return True

            # Not anagram. Shift +1 right. Update s2WindowLetters & remove if s2WindowLetters[letter] == 0 bc it should be removed to be equal to s1Letters
            s2WindowLetters[s2[l]] -= 1
            if s2WindowLetters[s2[l]] == 0:
                s2WindowLetters.pop(s2[l], 0)
            l += 1
            r += 1

        return False