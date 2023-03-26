n, k, m = map(int,input().split())

sum_of_det = 0

def excess_weight(n, k, m):
    k_lishn = n%k
    det_lishn = 0
    for i in range(0, n//k):
        det_lishn = det_lishn + k%m
    
    # Неиспользованная масса:
    excess = k_lishn + det_lishn
    return excess
    
def num_of_details(n, k, m):
    num_of_det = 0
    for i in range(0, n//k):
        num_of_det = num_of_det + k//m
    
    return num_of_det

#clown moment
for i in range(0, 200):
    sum_of_det = sum_of_det + num_of_details(n, k, m)
    n = excess_weight(n, k, m)

print(sum_of_det)
