class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       # Anagram = all letters are same, unordered
       # Make each str a set of letters + group matching sets
       # Hashmap setLetters:[words] 

       # CANNOT USE SET AS dict key bc it's mutable
       # Sort str so alphabetical + use as key. All anagrams will be the same alphabetically

        anagrams = defaultdict(list)
        for s in strs: 
            anagrams[str(sorted(s))].append(s)
        print(anagrams)
        res = []
        for key in anagrams:
            res.append(anagrams[key])
        return res