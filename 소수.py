num = int(input())

ch = [0] * (num+1)
cnt =0
for i in range(2,num+1):
    if ch[i] == 0:
        cnt +=1
        for j in range(i,num+1,i):
            ch[j] +=1
print(cnt)