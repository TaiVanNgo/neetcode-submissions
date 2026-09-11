class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # Loop through string
        for ch in s:
            if (
                ch == '(' 
                or ch == '[' 
                or ch == '{'
            ):
                stack.append(ch)
            elif(
                ch == ')'
                or ch == ']'
                or ch == '}'
            ):
                # if stack is empty at this point-> fail
                if stack:
                    top = stack.pop()
                else: 
                    return False
                print(ch)
                print(top)
                # compare
                if(
                    top == '(' and ch == ')'
                    or top == '[' and ch == ']'
                    or top == '{' and ch == '}'
                ): 
                    continue
                else:
                    return False

        # if stack is not empty
        if stack:
            return False

        return True
