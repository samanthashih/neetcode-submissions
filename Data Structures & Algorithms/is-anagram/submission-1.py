class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check: if lengths !=, then def NOT anagram
        if len(s) != len(t):
            return False

        # Solution 1: hashmap
        # - Fill hashmap(letter: count) per str. -> O(n) time
        # - Compare 2 hashmaps: if equal, then anagram. else, false -> O(n)

        s_letters = dict()
        t_letters = dict()

        for letter in s:
            if letter in s_letters:
                s_letters[letter] += 1
            else:
                s_letters[letter] = 1


        for letter in t:
            if letter in t_letters:
                t_letters[letter] += 1
            else:
                t_letters[letter] = 1
        
        if s_letters == t_letters:
            return True
        else:
            return False

        # Solution 2: sort alphabetical
        # - Sort each str letters alphabetical -> O(nlogn)
        # - Compare each sorted str. if equal, then anagram. else, false -> O(n)