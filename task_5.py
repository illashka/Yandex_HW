# Зовите меня — клоун
a1, b1, a2, b2 = map(int,input().split())

lptp1 = [a1, b1]
lptp2 = [a2, b2]
#10 2 
#2 10
var1 = [(lptp1[0]+lptp2[0]) * max(lptp1[1], lptp2[1])]
var2 = [(lptp1[0]+lptp2[1]) * max(lptp1[1], lptp2[0])]
var3 = [(lptp1[1]+lptp2[0]) * max(lptp1[0], lptp2[1])]
var4 = [(lptp1[1]+lptp2[1]) * max(lptp1[0], lptp2[0])]

values = [var1[0], var2[0], var3[0], var4[0]]
min_var = min(values)

if min_var == var1[0]:
    print((lptp1[0]+lptp2[0]), max(lptp1[1], lptp2[1]))
elif min_var == var2[0]:
    print((lptp1[0]+lptp2[1]), max(lptp1[1], lptp2[0]))
elif min_var == var3[0]:
    print((lptp1[1]+lptp2[0]), max(lptp1[0], lptp2[1]))
elif min_var == var4[0]:
    print((lptp1[1]+lptp2[1]), max(lptp1[0], lptp2[0]))
