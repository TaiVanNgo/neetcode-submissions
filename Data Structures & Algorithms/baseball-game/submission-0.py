class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for op in operations:
            if op == '+':
                # take the two most top values to add
                top_val = stack[-1] 
                secondtop_val = stack[-2]
                result = int(top_val+secondtop_val)
                stack.append(result)
            elif op == 'D':
                # take the top value
                top_val = stack[-1] 
                result = int(top_val*2)
                stack.append(result)
            elif op == 'C':
                stack.pop() # remove the top value
            else:
                stack.append(int(op))

        sum = 0 
        for num in stack:
            sum  = sum + num
        
        return sum
