func isUgly(num int) bool {
    if num < 1 {
        return false
    }
    if num < 7 {
        return true
    }

    if num % 2 == 0 {
        num /= 2
    } else if num % 3==0 {
        num /= 3
    } else if num % 5 == 0 {
        num /= 5
    } else {
        return false
    }
    return isUgly(num)
}