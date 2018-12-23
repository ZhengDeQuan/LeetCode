class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
        elif x == 0:
            return True
        else:
            div = 1
            while x // div >= 10:
                div *= 10
            print("div = ",div)
            while x > 0:
                front = x//div
                tail = x % 10
                if front != tail:
                    return False
                x -= front * div
                x //= 10
                div /= 100
            return True


if __name__ == "__main__":
    A = Solution()
    ret = A.isPalindrome(1001)
    print("ret = ",ret)
