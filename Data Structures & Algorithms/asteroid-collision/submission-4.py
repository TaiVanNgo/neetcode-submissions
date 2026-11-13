class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if ast > 0:
                stack.append(ast)

            if ast < 0: 
                # when the current stack is empty or the highest value is negative -> not collide
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(ast)
                else:
                    while stack and ast < 0 and stack[-1] > 0:
                        if stack[-1] > abs(ast):
                            ast = 0 # ast loses
                        elif stack[-1] < abs(ast):
                            stack.pop()
                        else: #if tie
                            ast = 0
                            stack.pop()

                    if ast:  # if ast is different to zero
                        stack.append(ast)

        return stack
