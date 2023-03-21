a ,b  = map(int,input().split())
cnt= [0]*(a*b+1)
max = -1
for i in range(1,a+1):
    for j in range(1,b+1):
        cnt[i+j]+=1
for i in range(a+b+1):
    if cnt[i]> max:
        max =cnt[i]
for i in range(a+b+1):
    if cnt[i] == max:
        print(i,end = ' ')