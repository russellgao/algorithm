# 单调栈
def dailyTemperatures(T: [int]) -> [int]:
    n = len(T)
    result = [0] * n
    stack = []
    for i in range(n):
        while stack and T[stack[-1]] < T[i]:
            tmp = stack.pop()
            result[tmp] = i - tmp
        stack.append(i)
    return result

if __name__ == "__main__" :
    T = [73,74,75,71,69,72,76,73]
    result = dailyTemperatures(T)
    print(result)