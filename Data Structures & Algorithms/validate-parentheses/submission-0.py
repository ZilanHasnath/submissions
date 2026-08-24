class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)
            
            elif len(stack) == 0:
                return False
            
            else:
                char = stack.pop()
                if (bracket == ')' and char == '(') or \
                   (bracket == '}' and char == '{') or \
                   (bracket == ']' and char == '['):
                    continue
                else:
                    return False

        return len(stack) == 0