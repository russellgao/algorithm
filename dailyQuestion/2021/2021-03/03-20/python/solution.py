class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        stack = []
        for i in range(len(tokens)) :
            tmp = tokens[i]
            if tmp == "+" :
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 + num1)
            elif tmp == "-" :
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif tmp == "*" :
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 * num1)
            elif tmp == "/" :
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
            else :
                stack.append(int(tmp))
        return stack[0]

if __name__ == "__main__" :
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    s = Solution()
    res = s.evalRPN(tokens)
    print(res)
