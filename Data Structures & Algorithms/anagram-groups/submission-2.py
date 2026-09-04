class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each word -> equal sorted words are anagrams  O(m * nlogn)
        # store anagrams in dict { sorted_word : [og words]}

        # represent each word by array of letter_counts=[a, b, c, ..., z]  O(m*n)
                # -> need to tuple([letter counts]) to use as dict key bc lists are mutable so not hashable
            # or by dict of letter_counts={a:0 , b:0, c:0, ...}
        # store anagrams in dict { letter_counts : [og words]}
        anagrams = defaultdict(list)

        for word in strs:
            letters = [0]*26

            for char in word:
                letters[ord(char) - ord('a')] += 1
            anagrams[tuple(letters)].append(word)
        
        return list(anagrams.values())


