
ptr = 0

def decodeString(s: str) -> str :
    """

    :param s:
    :return:
    """
    def getDigits() :
        global ptr
        global s
        ret = 0
        while s[ptr] >= "0" and s[ptr] <= "9" :
            ret = ret * 10 + int(s[ptr])
            ptr += 1
        return ret

    def getString() :
        global s
        global ptr
        if len(s) == ptr or s[ptr] == "]" :
            return ""
        current = s[ptr]
        result = ""
        if current >= "0" and current <= "9" :
            repeat = getDigits()
            ptr += 1
            s1 = getString()
            ptr += 1
            result = s1 * repeat
        elif (current >= "a" and current <= "z") or current >= "A" and current <= "A" :
            result = current
            ptr += 1
        return result + getString()

    return getString()

if __name__ == "__main__" :
    s = "12[a]2[bc]"
    result = decodeString(s)
    print(result)

