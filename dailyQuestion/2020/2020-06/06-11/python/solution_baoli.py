# 暴力法
def dailyTemperatures(T: [int]) -> [int]:
    n = len(T)
    result = [0] * n
    for i in range(n-1) :
        for j in range(i+1,n) :
            if T[j] > T[i] :
                result[i] = j-i
                break
    return result

if __name__ == "__main__" :
    T = [73,74,75,71,69,72,76,73]
    result = dailyTemperatures(T)
    print(result)