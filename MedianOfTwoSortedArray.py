'''
a[i-1],a[i]
b[j-1],b[j]

目标
a[i-1] <= b[j]
b[j-1] <= a[i]
i + j = (m + n) / 2
if (m + n) % 2 == 1 :
    return min(b[j],a[i])
if (m + n) %2 == 0:
    return ( max(b[j-1],a[i-1]) + min(b[j],a[i]) )  * 1.0 / 2.0

'''
def solve(nums1 ,nums2):
    '''
    :param l1: sorted list of int
    :param l2: sorted list of int
    :return:
    '''
    l1 = nums1
    l2 = nums2
    n = len(l1)
    m = len(l2)
    if n == 0:
        if m % 2 != 0:
            return l2[int(m/2)]
        else:
            return (l2[int(m/2)] + l2[int(m/2)-1])/2
    elif m==0:
        if n%2 !=0:
            return l1[int(n/2)]
        else:
            return (l1[int(n/2)] + l1[int(n/2)-1])/2
    if n <= m:
        big = l2
        big_len = m
        small = l1
        small_len = n
    else:
        big = l1
        big_len = n
        small = l2
        small_len = m

    print("small = ",small)
    print("big = ",big)

    singleFlag = False
    total_len = n + m
    if total_len % 2 == 0:
        singleFlag = False
    else:
        singleFlag = True

    small_l, small_r = 0, small_len
    #  用小的那个数组二分

    while small_l <= small_r:
        i = (small_l + small_r) // 2
        j = total_len // 2 - i
        print("i = ", i , " j = ",j)
        if i < small_r and small[i] < big[j - 1]:
            # i 需要变大
            small_l = i + 1
        elif i > 0 and small[i - 1] > big[j]:
            # i 需要变小
            small_r = i - 1
        else:
            break
    if singleFlag:  # 奇数个数，所以取min(a[i],b[j])
        if i == small_len:
            return big[j]
        res = min(small[i], big[j])
        return res
    else:
        # return (min(a[i] ,b[j]) +  max(a[i-1],b[j-1])) / 2
        # 如果i==0 or j==0 要特判
        temp = 0
        if i == 0:
            temp = big[j - 1]
            return (min(small[i], big[j]) + temp) / 2
        elif i == small_len:
            if j > 0:
                return (b[j] + max(a[i-1],b[j-1]))/2
            return (small[small_len - 1] + big[0]) / 2# 这时j==0
        else:
            return (min(small[i] , big[j]) + max(small[i-1] , big[j-1]))/2








if __name__ == "__main__":
    a = [1,2]
    b = [-1,3]
    res = solve(a,b)
    print("res = ",res)



'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = nums1
        l2 = nums2
        n = len(l1)
        m = len(l2)
        if n == 0:
            if m % 2 != 0:
                return l2[int(m/2)]
            else:
                return (l2[int(m/2)] + l2[int(m/2)-1])/2
        elif m==0:
            if n%2 !=0:
                return l1[int(n/2)]
            else:
                return (l1[int(n/2)] + l1[int(n/2)-1])/2
        if n <= m :
            big = l2
            big_len = m
            small = l1
            small_len = n
        else:
            big = l1
            big_len = n
            small = l2
            small_len = m

        singleFlag = False
        total_len = n + m
        if total_len % 2 == 0:
            singleFlag = False
        else:
            singleFlag = True

        small_l ,small_r = 0 , small_len
        # 用小的那个数组二分

        while small_l <= small_r:
            i = (small_l + small_r) // 2
            j =  total_len// 2 - i
            if i < small_r and small[i] < big[j-1]:
                #i 需要变大
                small_l = i + 1
            elif i > 0 and small[i-1] > big[j]:
                #i 需要变小
                small_r = i - 1
            else :
                break
        if singleFlag : #奇数个数，所以取min(a[i],b[j])
            if i == small_len:
                return big[j] 
            res =  min(small[i],big[j])
            return res 
        else:
            # return (min(a[i] ,b[j]) +  max(a[i-1],b[j-1])) / 2
            # 如果i==0 or j==0 要特判
            temp = 0
            if i == 0:
                if j == big_len:
                    return (small[0] + big[big_len-1])/2
                temp = big[j-1]
                
                return (min(small[i],big[j]) + temp) /2
            elif i == small_len: 
                if j > 0:
                    return (big[j] + max(small[i-1],big[j-1]))/2
                return (small[small_len-1] + big[0])/2 #这时j==0
            else:
                return (min(small[i] , big[j]) + max(small[i-1] , big[j-1]))/2
        
'''
