'''
let b[i+1][j+1] denotes if s[0...i] matches p[0...j] then
if p[j] != "*":
    b[i+1][j+1] = b[i][j] and (p[j] == s[i] or p[j] == '.')
elif p[j] == '*':
    here    denote p[j-1] with x
    b[i+1][j+1] = b[i+1][j-1] and j > 0   #  s[0...i] matches p[0...j-2]  x* -> NULL
               or b[i+1][j]               #  s[0...i] matches p[0...j-1]  x* -> x
               or b[i][j+1] and (p[j-1] == s[i] or p[j-1] == '.')
               #  s[0...i-1] matches p[0...j] because p[j]=='*' so
               actually s[0...i-2] matches p[0...j-1] and s[i-1] == p[j-1] or p[j-1] == '.'
               so when the i = i + 1, p[j-1] should still matches the s[i] to let the matching logic go on


corner case:
b[0][0] = 1 : an empty string matches an empty string
b[i][0] = 0 for i in range(1,len(s)) : s[0..i] is not empty , p[0] is empty , can't match
b[0][j+1] = j > 0 and b[0][j-1] and p[j] == '*' : p[0...j-2,j-1,j] matches empty if p[0...j-2] matches empty and p[j] == '*'
'''


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        b = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        b[0][0] = True
        for i in range(0, len(s)):
            b[i+1][0] = False
        for j in range(1, len(p)):
            b[0][j + 1] = (j > 0) and b[0][j - 1] and p[j] == "*"


        for i in range(0, len(s)):
            for j in range(0, len(p)):
                if p[j] != '*':
                    b[i + 1][j + 1] = b[i][j] and (p[j] == s[i] or p[j] == '.')
                elif p[j] == '*':
                    print("s[i] = ",s[i]," p[j] = ",p[j] ," i = ",i," j = ",j)
                    print(b[i][j + 1])

                    b[i + 1][j + 1] = j > 0 and b[i + 1][j - 1] \
                                      or b[i + 1][j] \
                                      or b[i][j + 1] and j > 0 and (p[j - 1] == s[i] or p[j - 1] == '.')
        for ele in b:
            for e in ele:
                print(e,end = " ")
            print()
        return b[len(s)][len(p)]

if __name__ == "__main__":
    A = Solution()
    ret = A.isMatch('aab','c*a*b')
    print(ret)