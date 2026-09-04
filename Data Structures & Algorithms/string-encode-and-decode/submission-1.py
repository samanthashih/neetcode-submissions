class Solution:

    def encode(self, strs: List[str]) -> str:
        # can't just smush all strs into 1 string w/ separators bc separator can be part of strs
        # maybe hash each str + smush into 1 string w/ . separator -> any . in og strs will be hashed
            # no bc can't unhash (hash is one way)
        
        # delimiter = len(str)
        # start each appended str with its len
        # when decode we know the 1st char in str is the count delimiter and we can count from there
            # problem: double digit count like 10xxx -> delimiter looks like 1, not 10
            # need another delimiter > to let us know when count is over 
        res = ""
        for s in strs:
            res += str(len(s))
            res += ">"
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        while index < len(s):
            print("res: ", res)
            print("index: ", index)

            count = ""
            while s[index] != ">":
                count += s[index]
                index += 1
            count = int(count)
            
            res.append(s[index+1:index+count+1])
            index = index+count+1
        return res

# test case
strs = ["we","say",":","yes","!@#$%^&*()"]
encoded = Solution().encode(strs)
print(encoded)
print(Solution().decode(encoded))
