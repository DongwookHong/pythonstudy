num = int(input())

max = -1
def digit_sum(x):
    sum = 0
    while(x>0):
        sum += x%10
        x //=10
    return sum

def digit_sum2(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum


k = list(map(int,input().split()))
for i in range (num):
    t =digit_sum(k[i])
    if(max < t):
        max = t
        y= k[i]
print(y)