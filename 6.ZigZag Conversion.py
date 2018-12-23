a = "PAYPALISHIRING"
n = len(a)
i = 0

all_row_num = 4
row_num = 0
step = 1
dire = 1
temp_dict = {}
while i < n:

    if row_num not in temp_dict:
        temp_dict[row_num] = []
    temp_dict[row_num].append(a[i])
    i += 1

    if row_num == 0:
        dire = 1
    elif row_num == all_row_num - 1:
        dire = -1


    row_num += dire * step

ret = ""
for key , value in temp_dict.items():
    ret += ''.join(value)

