temp = [int(temp) for temp in input().split()]

regime = input()

if regime not in regimes or len(temp) != 2:
    exit()
else:
    if regime == 'freeze':
        print(min(temp))
    elif regime == 'heat':
        print(max(temp))
    elif regime == 'fan':
        print(temp[0])
    else:
        print(temp[1])
