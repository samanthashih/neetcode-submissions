class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # matching anagrams have same chars -> sort each word alphabetically & compare -> create group
        # group using dict -> anagrams = {sortedWord:[og words]}

        anagrams = defaultdict(list)

        for word in strs:
            sortedWord = str(sorted(word))

            anagrams[sortedWord].append(word)
        
        # return a list of the groups
        ans = []
        for anagram in anagrams:
            ans.append(anagrams[anagram])
        return ans

        

strs = ["act","pots","tops","cat","stop","hat"]
print(Solution().groupAnagrams(strs)) # [["hat"],["act", "cat"],["stop", "pots", "tops"]]