class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for ch in s:
            if ch in ['[', '(', '{']:
                my_stack.append(ch)
            else:
                if len(my_stack) == 0:
                    return False
                left_ch = my_stack.pop()
                if not (ch == ']' and left_ch == '[' or ch == ')'
                        and left_ch == '(' or ch == '}' and left_ch == '{'):
                    return False

        return len(my_stack) == 0
