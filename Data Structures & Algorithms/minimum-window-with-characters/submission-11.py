class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = Counter(t)
        def isValid(substring: str):
            substringCts = Counter(substring)
            for letter, count in t_counts.items():
                if letter not in substringCts or substringCts[letter] < count:
                    return False
            return True

        # Inc right to find any valid substring. Shrink left as much as possible while valid
        # Store min length + l,r

        l = 0
        r = 0
        minSubstring = len(s)
        resL = 0
        resR = len(s)-1

        while r < len(s):
            if not isValid(s[l:r+1]):
                print("not valid: ", s[l:r+1])
                r += 1
                continue
            # substring valid. Shrink left
            print("valid: ", s[l:r+1])
            if r-l+1 < minSubstring:
                minSubstring = r-l+1
                resL = l
                resR = r
            
            l += 1

        if isValid(s[resL:resR+1]):
            return s[resL:resR+1]

        return ""