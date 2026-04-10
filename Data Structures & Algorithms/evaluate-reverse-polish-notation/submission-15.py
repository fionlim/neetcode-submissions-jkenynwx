class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elem in tokens:
            if elem.lstrip('-+').isdigit():
                stack.append(int(elem))
            else:
                right_val = stack.pop()
                left_val = stack.pop()
                res = None
                if elem == '+':
                    res = left_val + right_val
                elif elem == '-':
                    res = left_val - right_val
                elif elem == '*':
                    res = left_val * right_val
                elif elem == '/':
                    if left_val / right_val < 0 and abs(left_val) % abs(right_val) > 0 :
                        res = (left_val // right_val) + 1
                    elif abs(left_val) >= abs(right_val):
                        res = left_val // right_val
                    else:
                        res = 0
                print(f'{left_val} {elem} {right_val}')
                print(res)
                stack.append(res)
        return stack[-1]