class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append([i,temperatures[i]])
            else:
                curr = [i, temperatures[i]]
                while (len(stack) != 0):
                    prev = stack.pop()
                    print("prev: ", prev, " curr: ", curr)
                    if curr[1] <= prev[1]:
                        break
                    else:
                        output[prev[0]] = curr[0] - prev[0]

                if curr[1] > prev[1]:
                    stack.append(curr)
                else:
                    stack.append(prev)
                    stack.append(curr)

        return output