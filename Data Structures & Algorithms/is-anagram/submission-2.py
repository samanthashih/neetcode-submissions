class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edit: if lengths !=, then def NOT anagram
        if len(s) != len(t):
            return False

        # Solution 1: hashmap
        # - Fill hashmap(letter: count) per str. -> O(n) time
        # - Compare 2 hashmaps: if equal, then anagram. else, false -> O(n)

        s_letters = dict()
        t_letters = dict()

        # Edit: we now know lens ==. So we can loop once for i in range(len)
        for i in range(0, len(s)): # O(n)
            s_char = s[i]
            t_char = t[i]

            if s_char in s_letters:
                s_letters[s_char] += 1
            else:
                s_letters[s_char] = 0

            if t_char in t_letters:
                t_letters[t_char] += 1
            else:
                t_letters[t_char] = 0
        
        if s_letters == t_letters: # O(n)
            return True
        else:
            return False

        # Solution 2: sort alphabetical
        # - Sort each str letters alphabetical -> O(nlogn)
        # - Compare each sorted str. if equal, then anagram. else, false -> O(n)