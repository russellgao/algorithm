def findLongestSubarray(array: [str]) -> [str]:
    if not array:
        return []
    dp = [0] * len(array)
    dp[0] = 1 if (array[0] >= "A" and array[0] <= "Z") or (array[0] >= "a" and array[0] <= "z") else -1
    for i in range(1, len(array)):
        dp[i] = dp[i - 1] + 1 if (array[i] >= "A" and array[i] <= "Z") or (array[i] >= "a" and array[i] <= "z") else dp[i - 1] - 1
    mappings = {0: -1}
    for i in range(len(dp)):
        mappings[dp[i]] = mappings.get(dp[i], i)
    maxlength = 0
    left = 0
    right = 0
    for i in range(len(dp)):
        if i - mappings[dp[i]] > maxlength:
            left = mappings[dp[i]]
            right = i + 1
            maxlength = right - left
    return array[left + 1:right]

if __name__ == "__main__" :
    array = ["42","10","O","t","y","p","g","B","96","H","5","v","P","52","25","96","b","L","Y","z","d","52","3","v","71","J","A","0","v","51","E","k","H","96","21","W","59","I","V","s","59","w","X","33","29","H","32","51","f","i","58","56","66","90","F","10","93","53","85","28","78","d","67","81","T","K","S","l","L","Z","j","5","R","b","44","R","h","B","30","63","z","75","60","m","61","a","5","S","Z","D","2","A","W","k","84","44","96","96","y","M"]
    result = findLongestSubarray(array)
    print(result)
