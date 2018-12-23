class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX_INT = 2 ** 31 - 1
        MIN_INT = - (2 ** 31)
        length = len(str)
        if length == 0:
            return 0
        i = 0
        while i < length and str[i].isspace():
            i += 1
        flag = False
        num = 0
        if i == length:
            return 0
        if str[i] == '-':
            flag = True
        elif str[i] == '+':
            flag = False
        elif '0' <= str[i] <= '9':
            num = int(str[i])
        else:
            return 0
        i += 1
        while i < length:
            if '0' <= str[i] <= '9':
                num = num * 10 + int(str[i])
                i += 1
                if num > MAX_INT and flag is False:
                    return MAX_INT
                if -num < MIN_INT and flag is True:
                    return MIN_INT
            else:
                if flag is False:
                    return num
                return -num

        if flag is False:
            return num
        return -num
