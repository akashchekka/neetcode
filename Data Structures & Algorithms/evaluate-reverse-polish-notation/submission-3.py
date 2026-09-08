class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []

        def compute(a, b, op):
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            else:
                return int(a/b)
        
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(compute(a, b, token))

        return stack[0]
        
