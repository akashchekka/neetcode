class Solution:
    def isValid(self, s: str) -> bool:
        pdict = dict()
        pdict['{'] = '}'
        pdict['['] = ']'
        pdict['('] = ')'
        
        stack = []

        for i in s:
            if i != '}' and i != ']' and i != ')':
                stack.append(i)
            else:
                if not stack:
                    return False
                    
                temp = stack.pop()
                mappedone = pdict[temp]

                if mappedone != i:
                    return False

        return len(stack) == 0