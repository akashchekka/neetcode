class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""

        for i in s:
            if i.isalpha() or i.isdigit():
                temp += i.lower()

        i, j = 0, len(temp) - 1

        res = True

        while i <= j:
            if temp[i] != temp[j]:
                res = False
                break
            i += 1
            j -= 1

        return res