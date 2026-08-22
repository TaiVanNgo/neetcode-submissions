class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)

            else:
                if(len(stack) == 0):
                    return False

                popped_char = stack.pop()

                if (
                    popped_char == '('
                    and c == ')'
                    or popped_char == '{'
                    and c == '}'
                    or popped_char == '['
                    and c == ']'
                ):
                    continue
                else:
                    return False
        
        if len(stack) > 0: 
            return False
            
        return True
