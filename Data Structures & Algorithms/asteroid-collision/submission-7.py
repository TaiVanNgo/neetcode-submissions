class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)

            if a < 0:
                # no collision
                if stack and stack[-1] < 0 or len(stack) == 0:
                    stack.append(a)
                # There's will be collision
                else:
                    while(stack and a and stack[-1] > 0):
                        if stack[-1] > abs(a):
                            a = 0;
                        elif stack[-1] < abs(a):
                            stack.pop()
                        else:
                            stack.pop()
                            a = 0

                    if a:
                        stack.append(a)

        return stack      

            
