class Solution: #1/7/26
    def isAnagram(self, s: str, t: str) -> bool:
        # alphabetically sort strs O(2*nlogn) -> compare O(n)
        
        # dict of letter counts O(n) -> compare dicts O(n)
        
        if len(s) != len(t): # must be same length
            return False 

        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for i in range(len(s)):
            count_s[s[i]] += 1
            count_t[t[i]] += 1
        
        if len(count_s) != len(count_t): # count of unique letters must be same length
            return False 
        
        for letter, count in count_s.items():
            if count_t[letter] != count:
                return False

        return True

# tests
res1 = Solution().isAnagram("racecar", "carrace") # True
print(res1)

res2 = Solution().isAnagram("jar", "jam") # False
print(res2)