def solve():
    MAX_INT = (2 ** 31 -1)
    MIN_INT = - (2 ** 31)
    x = -100
    flag = False
    if x < 0:
        x = -x
        flag = True
    ret = []
    while x > 0:
        ret.append(x%10)
        x = x//10


    res = 0
    for ele in ret:
        res = res * 10 + ele
        if res > MAX_INT:
            return MAX_INT
        elif res < MIN_INT:
            return MIN_INT
    if flag:
        res = -res
    return res