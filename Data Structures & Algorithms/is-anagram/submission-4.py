class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort s & t alphabetically - O(2 * nlogn) n=len(s/t) -> compare
        # count letter occurrences of s & t - O(2 * n) -> compare counts

        # count as list[26 ints, each represent letter count] -> compare
            # comparison time complexity could be O(1) best case if len of lists !=
            # but here the lens will always be 26... so doesn't matter
        # count as dict{letter:count} -> iterate over and compare
            # comparison time complexity can be < 26, max 26 entries per dict


        # if len(s) != len(t) -> definitely not anagrams -> return False
        if len(s) != len(t):
            return False 


        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for char in s: # O(n)
            count_s[char] += 1

        for char in t: # O(n)
            count_t[char] += 1

        for letter, count in count_s.items(): # O(26)
            if count_t[letter] != count:
                return False
        # couldve just done count_s == count_t (python will compare dicts no matter order)
        
        return True

        

# Test case 1
s = "racecar"
t = "carrace"
print(Solution().isAnagram(s, t)) # true

