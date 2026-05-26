class Solution:

    PLACEHOLDER = -999

    def calculate(self, left, right, op):
        left = int(left)
        right = int(right)
        if op == "+":
            return left + right
        elif op == "-":
            return left - right
        elif op == "*":
            return left * right
        else:
            return math.trunc(left / right)

    def is_op(self, char):
        return char in ["+", "-", "*", "/"]

    def evalRPN(self, tokens: List[str]) -> int:
        storage = []
        left = self.PLACEHOLDER
        right = self.PLACEHOLDER
        op = self.PLACEHOLDER

        while len(tokens) != 0:
            char = tokens.pop()

            # check if the char is an operator
            if self.is_op(char):
                # if i have no operator yet i use it
                if op == self.PLACEHOLDER:
                    op = char
                # if i already have an operator, means need to perform another operation first
                else:
                    if op != self.PLACEHOLDER:
                        storage.append(op)
                    if right != self.PLACEHOLDER:
                        storage.append(right)
                    op = char
                    right = self.PLACEHOLDER
                    # print(storage)
            # not an operator
            else:
                if op == self.PLACEHOLDER:
                    return int(char)

                if left == self.PLACEHOLDER and right != self.PLACEHOLDER:
                    left = char
                    # print("left becomes: ", left)
                else:
                    right = char
                    # print("right becomes: ", right)

                # print(left, right)
                
                # if i have the necessary values, i perform the operation
                if left != self.PLACEHOLDER and right != self.PLACEHOLDER and op != self.PLACEHOLDER:
                    # print(left, op, right)
                    val = self.calculate(left, right, op)
                    storage.append(str(val))

                    # reset left, right, op
                    left = self.PLACEHOLDER
                    right = self.PLACEHOLDER
                    op = self.PLACEHOLDER

                    # push everything in temp storage back into tokens in correct order (from the back)
                    storage.reverse()
                    tokens.extend(storage)
                    storage = []

        return 400
        