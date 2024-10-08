class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        for char in s:
            if char == ')':
                rev = ""
                while stack and stack[-1] != '(':
                    rev += stack.pop()
                if stack:
                   stack.pop()  # pop the opening bracket
                for c in rev:
                    stack.append(c)
            else: 
                stack.append(char)

        return ''.join(stack)
    

### INCORRECT ###