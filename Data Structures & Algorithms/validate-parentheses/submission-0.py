class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'(': ')', '{': '}', '[':']'}
        for i in range(len(s)):
            next_char = s[i]

            # if stack is empty theres nothing to check
            if len(stack) != 0:
                check = stack.pop()
                if check in dict and dict[check] == next_char:
                    continue
                stack.append(check)
                
            stack.append(next_char)

        return len(stack) == 0
