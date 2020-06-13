def groupAnagrams(strs: [str]) -> [[str]]:
    if not strs :
        return [[]]
    result_tmp = {}
    for item in strs :
        tmp = "".join(sorted(item))
        if tmp in result_tmp :
            result_tmp[tmp].append(item)
        else :
            result_tmp[tmp] = [item]
    result = list(result_tmp.values())
    return result

if __name__ == "__main__" :
    strs = ["eat","tea","tan","ate","nat","bat"]
    result = groupAnagrams(strs)
    print(result)


