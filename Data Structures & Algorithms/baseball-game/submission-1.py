class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for point in operations:
            if point == "+":
                stack.append(stack[-1] + stack[-2])
            elif point == "D":
                stack.append(stack[-1]*2)
            elif point == "C":
                stack.pop()
            else:
                stack.append(int(point))

        sum = 0
        for p in stack:
            sum = sum + p
        
        return sum