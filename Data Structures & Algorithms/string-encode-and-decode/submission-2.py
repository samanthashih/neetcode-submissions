class Solution:

    def encode(self, strs: List[str]) -> str:
        # need delimiter between strs 
        # -> can't use reg char like / bc / could be part of a str and would mess up decode

        # hash(str) + delimiter -> hashed str would only be alphanumeric so / delimeter is ok
            # :( cannot unhash the encoded str. Hash is one-way
        
        # for each char in word -> append ord(char) which is a number. Use - delimiter btwn ords, ' ' delimiter btwn words
        encoded_strs = ""
        for s in strs:
            for char in s:
                encoded_strs += (str(ord(char)) + '-')
            encoded_strs += " "
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        # separate into ord words by ' ' delimeter
        # separate ord words into each ord by '-' delimiter
        # for each ord word, chr(ord_val) back into og word
        res = []
        ord_words = s.split(' ')
        for j in range(len(ord_words)-1): # start decoding 1 word at a time. Skip last value since it's just ''
            ord_word = ord_words[j]
            word = ""

            ord_vals = ord_word.split('-')
            for j in range(len(ord_vals)-1): # rebuild og word char by char. Skip last value since it's just ''
                ord_val = ord_vals[j]
                word += chr(int(ord_val))
            res.append(word)

        return res



dummy_input = ["Hello","World"]
encoded = Solution().encode(dummy_input)
print(Solution().decode(encoded))