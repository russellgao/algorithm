
# 利用栈(stack) 进行求解 进行
def decodeString(s: str) -> str:
    def is_num(num):
        if num >= '0' and num <= '9':
            return True
        return False

    stack = []
    for i in range(len(s)):
        if s[i] == "]":
            s1 = ""
            num = ""
            while stack[-1] != "[":
                s1 = stack.pop() + s1
            stack.pop()
            while len(stack) != 0 and is_num(stack[-1]):
                num = stack.pop() + num
            s1 = s1 * int(num)
            stack.append(s1)
        else:
            stack.append(s[i])
    return "".join(stack)

if __name__ == "__main__" :
    s = "3[a]2[bc]"
    result = decodeString(s)
    print(result)