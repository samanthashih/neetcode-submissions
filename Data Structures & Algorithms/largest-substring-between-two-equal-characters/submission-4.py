class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = defaultdict(list)
        maxLength = -1

        for i, letter in enumerate(s):
            seen[letter].append(i)

        print(seen)
        for key, val in seen.items():
            val.sort()
            if len(val) >= 2:
                maxLength = max(maxLength, val[-1]-val[0]-1)
                print("maxLength: ", maxLength)

        return maxLength