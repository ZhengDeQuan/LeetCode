import pdb
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    temp_list = []
    max_l = 0
    now_l = 0
    for ch in s:
        print("ch = ",ch)
        # pdb.set_trace()
        if ch not in temp_list:
            temp_list.append(ch)
            now_l += 1
            if now_l > max_l:
                max_l = now_l
            print("temp_list = ",temp_list , "  now_l = ",now_l)

        else:
            while ch in temp_list:
                temp_list.pop(0)
                now_l -= 1
                print("now_l_2  = ", now_l)
            temp_list.append(ch)
            now_l += 1
    return max_l

if __name__ == "__main__":
    s = "pwwkew"
    s = "abcabcbb"
    res = lengthOfLongestSubstring(s)
    print(res)
    # print(ch)