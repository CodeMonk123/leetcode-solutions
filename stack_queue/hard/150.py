from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        fn_table = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y),
        }

        for token in tokens:
            if token.isdigit() or (len(token) > 0 and token[0] == '-'
                                   and token[1:].isdigit()):
                s.append(int(token))
            else:
                op1 = s.pop()
                op2 = s.pop()
                s.append(fn_table[token](op2, op1))
                print(s)
        return s.pop()


solution = Solution()
print(
    solution.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
