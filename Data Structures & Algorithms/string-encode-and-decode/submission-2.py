class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''

        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        while j < len(s):
            if s[j].isdigit():
                j += 1
                continue
            if s[j] == '#':
                num = int(s[i:j])
                res.append(s[j + 1: j + 1 + num])
                j = j + 1 + num
                i = j

        return res