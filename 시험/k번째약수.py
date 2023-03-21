num , mini = map(int , input().split())

cnt =0
for i in range(1,num):
    if(num % i==0):
        cnt+=1
    if(cnt == mini):
        print(i)
        break
else:
    print(-1)



