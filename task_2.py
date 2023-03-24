side_len = [int(x) for x in input().split()]

if  side_len[0] + side_len[1] > side_len[2] and \
    side_len[0] + side_len[2] > side_len[1] and \
    side_len[1] + side_len[2] > side_len[0]:
    print('YES')
else:
    print('NO')
