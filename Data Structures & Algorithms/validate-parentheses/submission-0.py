class Solution:
    def isValid(self, s: str) -> bool:
        left_stack = []
        right_stack = []
        for char in s:
            left_stack.append(char)
        for i in range(len(left_stack)):
            char = left_stack.pop()
            if char in [']', ')', '}']:
                right_stack.append(char)
            elif char in ['[', '(', '{'] and right_stack:
                match_char = right_stack.pop()
                if char + match_char not in ['[]', '()', '{}']:
                    return False
            else:
                return False
        if len(right_stack) > 0:
            return False
        return True