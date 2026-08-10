class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []

        temps = temperatures

        for i, t in enumerate(temps):
            #print("for:", "i:", i, "t:", t, "temps:", temps, "stack:", stack, sep=" ")
            if stack:
                while stack and t > stack[-1][1]:
                    temps[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
            stack.append((i, t))

        for i, t in stack:
            temps[i] = 0

        return temps