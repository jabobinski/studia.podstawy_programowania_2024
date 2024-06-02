class ValidParentheses:
    def is_valid(self, s):
        stack = []
        parentheses_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in parentheses_map.values():
                stack.append(char)
            elif char in parentheses_map:
                if not stack or stack[-1] != parentheses_map[char]:
                    return False
                stack.pop()
            else:
                return False
        return not stack

validator = ValidParentheses()
print(validator.is_valid("()"))     
print(validator.is_valid("()[]{}")) 
print(validator.is_valid("[)"))      
print(validator.is_valid("({[)]"))  
print(validator.is_valid("{{{"))   