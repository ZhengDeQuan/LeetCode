
class Solution:
    def preprocess(self, s):
        ret = "^#"
        for ch in s:
            ret += ch
            ret += "#"
        ret += '?'
        return ret

    def postprocess(self, s, center, d):
        ret = s[center - d:center + d + 1]
        ret = ret.split('#')
        return ''.join(ret)

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s
        s = self.preprocess(s)
        C = 0
        R = 0
        max_len = 0
        max_center = 0
        length = len(s)
        P = []
        for i in range(length):
            P.append(0)
            if i < R:
                P[i] = int(min(P[2 * C - i], R - i))
            else:
                P[i] = 1
            while i - P[i]>=0 and i + P[i] < length and s[i + P[i]] == s[i - P[i]]:
                P[i] += 1
            P[i] = int(max(P[i]-1 , 0))
            if i + P[i] > R:
                C = i
                R = i + P[i]
            if P[i] > max_len:
                max_len = P[i]
                max_center = i
        ret = self.postprocess(s, max_center, max_len)
        return ret


if __name__ == "__main__":
    Ex = Solution()
    a = "ababd"
    ret = Ex.longestPalindrome(a)
    print("ret = ",ret)