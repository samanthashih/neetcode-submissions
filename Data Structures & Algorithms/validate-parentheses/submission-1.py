class Solution:
    def isValid(self, s: str) -> bool:
        # need to find pairs of brackets
        # stack -> we encounter open ( -> push to stack
            # we encounter ) -> pop stack, check if matching pair 
            # if match -> continue thru s
            # else -> not a pair, invalid order

        openBrackets = {
            '(':')',
            '{':'}',
            '[':']'
            }
        closedBrackets = {')', '}', ']'}

        bracketsStack = []
        
        for char in s:
            if char in openBrackets:
                bracketsStack.append(char)
            elif char in closedBrackets:
                if len(bracketsStack) == 0:
                    return False
                
                if openBrackets[bracketsStack.pop()] != char:
                    return False
            else: # invalid char
                return False

        if len(bracketsStack) != 0: # check we matched all remaining pairs
            return False

        
        return True